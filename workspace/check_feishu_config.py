#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查飞书配置并使用API删除应用
"""

import os
import json
import requests
import yaml


def check_feishu_config():
    """检查飞书配置"""
    config_paths = [
        'workspace/channels/feishu.yml',
        'channels/feishu.yml',
        '../channels/feishu.yml'
    ]

    for path in config_paths:
        full_path = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(full_path):
            print(f"找到配置文件: {full_path}")

            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # 检查是否已配置
                    if 'cli_axxxxxxxxxxxxxxx' in content:
                        print("✗ AppID未配置（仍为占位符）")
                        return None
                    elif 'cli_a' in content:
                        # 解析YAML
                        try:
                            config = yaml.safe_load(content)
                            if config and 'appId' in config:
                                print(f"✓ 找到AppID: {config['appId'][:20]}...")
                                return config
                        except:
                            pass
            except Exception as e:
                print(f"✗ 读取配置失败: {e}")

    print("✗ 未找到有效的飞书配置")
    return None


def list_feishu_apps(app_id, app_secret):
    """获取飞书应用列表

    Args:
        app_id: 飞书应用ID
        app_secret: 飞书应用密钥

    Returns:
        list: 应用列表
    """
    # 这里需要调用飞书API获取应用列表
    # 但是需要开发者权限

    # 飞书API地址
    api_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

    # 请求获取tenant_access_token
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }

    try:
        response = requests.post(api_url, json=payload)
        result = response.json()

        if result.get('code') == 0:
            token = result.get('tenant_access_token')
            print(f"✓ 获取到tenant_access_token")

            # 使用token获取应用列表
            # 注意：这需要管理员权限
            apps_api = "https://open.feishu.cn/open-apis/bot/v3/apps/list"
            headers = {
                "Authorization": f"Bearer {token}"
            }

            apps_response = requests.get(apps_api, headers=headers)
            apps_result = apps_response.json()

            if apps_result.get('code') == 0:
                return apps_result.get('data', {}).get('app_list', [])
            else:
                print(f"✗ 获取应用列表失败: {apps_result.get('msg')}")
                return []
        else:
            print(f"✗ 获取token失败: {result.get('msg')}")
            return []
    except Exception as e:
        print(f"✗ API调用失败: {e}")
        return []


def delete_feishu_app(app_id, app_secret, target_app_id):
    """删除飞书应用

    Args:
        app_id: 飞书应用ID
        app_secret: 飞书应用密钥
        target_app_id: 要删除的应用ID

    Returns:
        bool: 是否删除成功
    """
    # 这里需要调用飞书API删除应用
    # 但是需要开发者权限

    print(f"尝试删除应用: {target_app_id}")

    # 注意：飞书API可能不支持通过API删除应用
    # 需要在开放平台网页上手动删除

    return False


def main():
    """主函数"""
    print("🦞 飞书应用删除工具（API方式）")
    print("="*50)

    # 1. 检查配置
    print("\n📋 检查飞书配置...")
    config = check_feishu_config()

    if not config:
        print("\n❌ 飞书未配置，无法使用API方式")
        print("\n请使用浏览器方式删除应用:")
        print("1. 打开 https://open.feishu.cn/")
        print("2. 登录并找到'我的应用'")
        print("3. 手动删除作废的应用")
        return

    # 2. 获取应用列表
    print("\n📋 获取应用列表...")
    app_id = config.get('appId')
    app_secret = config.get('appSecret')

    if not app_id or not app_secret:
        print("✗ AppID或AppSecret未配置")
        return

    apps = list_feishu_apps(app_id, app_secret)

    if not apps:
        print("\n⚠️  未获取到应用列表")
        print("可能原因:")
        print("1. 该应用没有列出其他应用的权限")
        print("2. 该应用不是管理员")
        print("3. API不支持此操作")
        print("\n建议使用浏览器方式删除")
        return

    # 3. 显示应用列表
    print(f"\n找到 {len(apps)} 个应用:")
    for i, app in enumerate(apps):
        print(f"{i+1}. {app.get('app_name', 'Unknown')} (ID: {app.get('app_id', 'Unknown')})")

    # 4. 删除作废的应用
    print("\n🗑️  删除作废的应用...")
    deleted = 0

    for app in apps:
        app_name = app.get('app_name', '')
        app_id_to_delete = app.get('app_id', '')

        # 判断是否作废
        if is_obsolete(app_name):
            print(f"  删除: {app_name}")

            # 尝试删除
            if delete_feishu_app(app_id, app_secret, app_id_to_delete):
                deleted += 1
                print(f"    ✓ 已删除")
            else:
                print(f"    ✗ 删除失败，请手动删除")

    print(f"\n✓ 成功删除 {deleted} 个应用")


def is_obsolete(app_name):
    """判断应用是否作废"""
    if not app_name:
        return False

    obsolete_keywords = [
        'test', '测试', 'temp', '临时', 'demo', '演示',
        'sample', '样例', 'debug', '调试', 'old', '旧'
    ]

    app_name_lower = app_name.lower()

    for keyword in obsolete_keywords:
        if keyword in app_name_lower:
            return True

    return False


if __name__ == "__main__":
    main()
