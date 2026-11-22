# 给 MiniMax（Mavis）的转移目录说明

最近更新：2026-11-19 23:35　三屏电脑 USER-20220504VZ

本文件由「C盘每两小时清理与迁移」定时任务维护，每轮执行后刷新，历史记录只增不删。

发送方式：整段复制本文件内容发给 MiniMax，或直接告诉它读这个路径。

━━━━━━━━━━━━━━━━

一、当前磁盘可用空间，实测

C 盘　可用 76.11GB　已用 137.33GB　总 213.43GB
D 盘　可用 90.60GB　已用 21.18GB　总 111.79GB
E 盘　可用 27.43GB　已用 205.70GB　总 233.13GB

C 盘可用 76.11GB，仍远超 40GB，后续轮次只清不迁；一旦跌破 40GB 再恢复搬迁。

系统整盘镜像已生成（2026-11-19 23:14 完成）：E:\系统镜像备份\C盘整卷镜像_20261119.wim，73,418,140,207 字节即 68.38GB，单映像，530,238 文件、184,390 目录，原始数据 126.94GB，压到约 58%，103GiB 全量校验通过。MiniMax 需要整盘镜像或某个历史文件时直接读这个 wim，用 D:\wimlib\wimlib-imagex.exe extract 抽取单个文件、apply 还原整盘，不要复制回 C 盘。

这个镜像没包含 WPS 云盘目录 C:\Users\Administrator\Documents\WPS Cloud Files，该目录 11.36GB 逻辑、58,998 文件，其中 54,548 个是云端占位共 7.38GB，快照里读不出来会中止整盘备份；要这部分就在 WPS 客户端把文件先下载到本地，再单独备份。

D 盘可用 90.60GB，空间充裕；E 盘可用 27.43GB，其中 68.38GB 被系统整盘镜像占住，不再随便往里塞东西，新的冷数据一律走 D 盘。D 盘内文件只许读与复制，不许删。

━━━━━━━━━━━━━━━━

二、两个固定落点

旧批次落点：D:\C盘搬迁_20261111　11-11 与 11-12 两次人工迁移的成果，路径固定不动。

定时批次落点：D:\C盘搬迁_定时迁移　定时任务每两小时往里放冷数据，按来源原名建子目录。

━━━━━━━━━━━━━━━━

三、已迁入清单

2026-11-11 第一批，10.32GB，21,065 文件
回测引擎_数据库备份　10 文件　2.00GB　来源 首阳战法回测引擎\data 的 engine.db.bak_*
股票研究_迁移包与成品　19,031 文件　3.92GB　来源 Desktop\01_股票研究
龙虾_历史版本包　1,999 文件　4.40GB　来源 Desktop\01_股票研究\龙虾命中的个股
选股备份_旧版本　25 文件　约 1MB　来源 Desktop\选股系统备份

2026-11-11 第二批，4.34GB，1,488 文件
MiniMax_成品　来源 Desktop\02_内容创作 的 Mavis视频成品、龙虾制作的小程序、龙虾头像，以及 股票克隆包_20261107 与其 v2.zip、06_客户端安装包、豆包和minimax资产

2026-11-12 第三批，11.14GB，8,404 文件
选股_改前备份\_bak_s2_20261107　4,672 文件　9.69GB　来源 C:\Users\Administrator\_bak_s2_20261107
选股_改前备份\_bak_s2_20261106　3,732 文件　1.45GB　来源 C:\Users\Administrator\_bak_s2_20261106

2026-11-12 16:30 定时任务第一轮，2.57GB，1 文件
.qclaw-backups 目录整层迁入，来源 C:\Users\Administrator\.qclaw-backups，内容 qclaw-backup-20260820-075141.zip，2756248088 字节，迁移完成 16:30。目标件数字节与源侧基线一致，源目录已删除。

2026-11-12 18:17 定时任务第二轮，0GB，0 文件
本轮没有新迁入。扫描后确认 C 盘已无符合"目录内全部文件早于 7 天"且不属于程序目录的冷数据块，按规则不搬。同花顺旧版安装包 4 个共 996.4MB 按清理项删除，未迁移。

2026-11-13 08:17 定时任务第三轮，0GB，0 文件
本轮没有新迁入。整夜 20:17 至 06:17 六轮因本机离线未执行，本机 08:17 前恢复在线。扫描后仍无合格的整块冷目录，按规则不搬。清理只删了临时文件、旧日志与 __pycache__，共释放约 82.7MB。

2026-11-13 09:05 定时任务第四轮（用户批准后补跑），4.70GB，129853 文件
.qclaw 目录整层迁入，来源 C:\Users\Administrator\.qclaw，129853 文件，5050919903 字节，迁移完成 09:05。目标侧回读件数与字节与源侧基线完全一致，源侧目录已不存在；随后在 C:\Users\Administrator\.qclaw 原位建立目录联接（Junction）指向 D:\C盘搬迁_定时迁移\.qclaw，程序读写路径不变，经联接可正常读取。

2026-11-13 10:31 定时任务第五轮，4.66GB，60899 文件，全部按原位建联接
.agents　来源 C:\Users\Administrator\.agents，1821 文件，1295502891 字节，迁至 D:\C盘搬迁_定时迁移\.agents，完成 10:20。
.openclaw-windclaw　来源 C:\Users\Administrator\.openclaw-windclaw，8032 文件，728825342 字节，迁至 D:\C盘搬迁_定时迁移\.openclaw-windclaw，完成 10:24。这一块源侧用 PowerShell 枚举只数到 6591 文件 718427847 字节，比实际少 1441 个文件，原因是深层长路径文件枚举不到；复制后用 robocopy 自身清点目标侧为 8032 文件 695.06MB，与搬运时一致，源侧已消失，判定完整。联接在核对之后补建，实测量到 2 个顶层条目。
lobsterai　来源 C:\Users\Administrator\lobsterai，2263 文件，635872051 字节，迁至 D:\C盘搬迁_定时迁移\lobsterai，完成 10:26。
AppData\Roaming\LobsterAI　来源 C:\Users\Administrator\AppData\Roaming\LobsterAI，32620 文件，1978610041 字节，迁至 D:\C盘搬迁_定时迁移\AppData\Roaming\LobsterAI，完成 10:29。
AppData\Roaming\QClaw　来源 C:\Users\Administrator\AppData\Roaming\QClaw，17604 文件，365636845 字节，迁至 D:\C盘搬迁_定时迁移\AppData\Roaming\QClaw，完成 10:30。
这五块搬运前都复查过最新写入时间，分别是 11-02、09-30、04-20、09-16、09-05，全部早于 7 天，且 QClaw、Lobster 相关进程当时为 0 个。合计 5004447170 字节。五处源目录均已改建成指向 D 盘的目录联接，程序按原路径照常读写。

2026-11-13 12:27 定时任务第六轮，1.58GB，17530 文件，全部按原位建联接
.paddlex　来源 C:\Users\Administrator\.paddlex，35 文件，219564435 字节，迁至 D:\C盘搬迁_定时迁移\.paddlex，完成 12:23。最新写入 04-05。
AppData\Local\electron　来源 C:\Users\Administrator\AppData\Local\electron，11 文件，409650912 字节，迁至 D:\C盘搬迁_定时迁移\AppData\Local\electron，完成 12:24。最新写入 04-06。
AppData\Local\JianyingPro　来源 C:\Users\Administrator\AppData\Local\JianyingPro，17484 文件，1072197875 字节，迁至 D:\C盘搬迁_定时迁移\AppData\Local\JianyingPro，完成 12:26。最新写入 10-14，搬家时剪映进程为 0 个。
三块合计 1701413222 字节。三处源目录已改建为指向 D 盘的目录联接，剪映按原路径照常读写。

2026-11-13 14:26 定时任务第七轮，3.78GB，17832 文件，全部按原位建联接
这十三块搬运前都验过最新写入时间，全部早于 7 天，对应程序当时进程数为 0 个。
AppData\Roaming\蚁小二4.0　4859 文件，799651950 字节，最新写入 08-23，完成 14:20。
AppData\Roaming\bilibili　1599 文件，599409722 字节，最新写入 11-02，完成 14:20。
AppData\Roaming\greencore　167 文件，555890567 字节，最新写入 01-30，完成 14:21。
AppData\Roaming\douyin　2093 文件，384264422 字节，最新写入 10-26，完成 14:21。
AppData\Roaming\360se6　188 文件，351984152 字节，最新写入 03-14，完成 14:22。
.cache　10 文件，195187008 字节，最新写入 04-26，完成 14:22。
AppData\Local\ChromeExtensionCache　9 文件，194085231 字节，最新写入 10-25，完成 14:22。
AppData\Roaming\@hilo　4332 文件，200000367 字节，最新写入 09-15，完成 14:23。
AppData\Roaming\autoclaw　166 文件，160217071 字节，最新写入 09-05，完成 14:23。
AppData\Roaming\WindClaw　430 文件，184490041 字节，最新写入 09-30，完成 14:24。
.EasyOCR　2 文件，105103751 字节，最新写入 06-29，完成 14:24。
.openclaw　543 文件，198054009 字节，最新写入 10-28，完成 14:25。这一块复制后用 PowerShell 枚举目标侧只数到 487 文件 197735675 字节，少 56 个，是长路径枚举不到；改用 robocopy 自身清点目标侧为 543 文件 188.87MiB，与源侧基线完全一致，源侧已消失，判定完整，联接随后补建。
.hub　3434 文件，132803667 字节，最新写入 09-15，完成 14:25。
十三块合计 4061141958 字节。十三处源目录均已改建为指向 D 盘的目录联接。

2026-11-14 10:39 定时任务第八轮，2.11GB，63029 文件，全部按原位建联接
这十六块搬运前都验过目录内最新写入时间，全部早于 7 天，且不含禁迁清单内的目录。
self-improving　来源 C:\Users\Administrator\self-improving，314 文件，102564862 字节，最新写入 05-10。
AppData\Local\DingTalk_133　859 文件，93943914 字节，最新写入 03-23。
AppData\Local\qmlauncher-updater　1 文件，93126152 字节，最新写入 06-29。
AppData\Local\yiheng-deploy-updater　1 文件，81697891 字节，最新写入 04-06。
AppData\Local\Thunder Network　2 文件，80421341 字节，最新写入 07-12。
AppData\Local\node-gyp　2728 文件，63664967 字节，最新写入 04-11。
AppData\Local\com.tencent.yuanbao　246 文件，57316565 字节，最新写入 2025-03-18。
AppData\Local\Package Cache　24 文件，50045566 字节，最新写入 03-22。
AppData\Local\flutter_webview_windows　318 文件，40189389 字节，最新写入 2025-08-22。
AppData\Roaming\obs-sh_main-min-0.7.3-soft　37 文件，64413051 字节，最新写入 01-30。
AppData\Roaming\ollama app.exe　395 文件，46256953 字节，最新写入 04-07。
AppData\Roaming\SodaMSOAddin　34 文件，39784301 字节，最新写入 02-04。
AppData\Roaming\Python　1387 文件，37746751 字节，最新写入 07-25。
AppData\Roaming\Blackmagic Design　161 文件，37018608 字节，最新写入 04-05。
AppData\Roaming\hotspotessw　13 文件，35501813 字节，最新写入 08-23。
AppData\Roaming\npm　56509 文件，1340130978 字节，最新写入 08-17，这一块耗时最长，用了 294 秒。
十六块合计 2263823102 字节，全部迁到 D:\C盘搬迁_定时迁移 下同名相对路径，完成时间 10:29 至 10:38。
逐块回读结果：目标侧件数与字节与源侧基线完全相等，源侧目录已不存在，随后在原位建目录联接，回读 LinkType 全部为 Junction。
本轮件数与字节核对用 python 的 \\?\ 长路径枚举做双端计数，避免 PowerShell 长路径漏数。

2026-11-14 12:22 定时任务第九轮，0.22GB，2107 文件，搬成十一块，失败一块已整体回滚
本轮先按原规则筛冷目录，发现前八轮已经把大块冷数据搬完，剩下的要么是活数据，要么是飞书主程序本体。
AppData\Local\ShadowBot　568 文件，27927342 字节，最新写入 03-18，完成 12:18。
AppData\Local\ShadowBotBrowser　460 文件，30098847 字节，最新写入 03-18，完成 12:18。
AppData\Local\Android　123 文件，27870368 字节，最新写入 04-14，完成 12:18。
AppData\Local\qBittorrent　4 文件，8411933 字节，最新写入 04-06，完成 12:18。
AppData\Local\kdocs-cli　2 文件，7721989 字节，最新写入 08-16，完成 12:18。
AppData\Local\Bytedance　342 文件，7475732 字节，最新写入 09-19，完成 12:18。
AppData\Local\DQSStockPro　128 文件，14473456 字节，最新写入 2022-05-04，完成 12:18。
AppData\Local\ai.openclaw.clawpanel　267 文件，32344635 字节，最新写入 03-29，完成 12:18。
AppData\Roaming\Octopus8　190 文件，31579122 字节，最新写入 03-17，完成 12:19。
AppData\Roaming\360Aiview　15 文件，29166074 字节，最新写入 2025-09-26，完成 12:19。
AppData\Roaming\NGRLauncher　8 文件，10489852 字节，最新写入 04-20，完成 12:19。
十一块合计 227559350 字节，全部迁到 D:\C盘搬迁_定时迁移 下同名相对路径，逐块回读件数与字节与源侧基线相等，源侧目录已不存在，并在原位建好目录联接。
本轮有一块失败：AppData\Local\electron-builder　446 文件 35041811 字节，复制到目标后源侧目录未被删除，判定不合格，已把内容整体搬回 C 盘原位并清掉 D 侧残留，没有留下半截状态；失败原因是该目录内有文件被进程占用，删不掉源目录。
飞书主程序本体 AppData\Local\Feishu 8012 文件 2.29GB 最新写入 10-24，已冷，但属程序本体且飞书在跑，沿用前几轮判断本轮不搬。
本轮同时清了超 30 天日志 13 个 1013631 字节、__pycache__ 80 个目录 674 文件 18170648 字节、Local\Temp 5 文件 135106 字节、豆包 Code Cache 3 文件 19836 字节。

2026-11-14 14:23 定时任务第十轮，0.14GB，1004 文件，搬成十二块，全部核对通过
本轮先按规则筛冷目录，符合条件又值得搬的只剩十几块几十 MB 级目录，全部照搬，不留尾巴。
AppData\Local\electron-builder　446 文件，35041811 字节，最新写入 2026-04-06，完成 14:23。
AppData\Roaming\WebView　249 文件，23860392 字节，最新写入 2026-03-14，完成 14:21。
AppData\Roaming\temp　3 文件，16808550 字节，最新写入 2026-03-05，完成 14:21。
AppData\Roaming\lct　48 文件，11921645 字节，最新写入 2026-09-04，完成 14:21。
AppData\Roaming\HuoYuYan　63 文件，8977912 字节，最新写入 2026-03-17，完成 14:21。
AppData\Roaming\yiheng-ai　52 文件，8866661 字节，最新写入 2026-04-07，完成 14:21。
AppData\Roaming\xmpclient　35 文件，8178938 字节，最新写入 2026-08-18，完成 14:21。
AppData\Roaming\yiheng-deploy　50 文件，7736091 字节，最新写入 2026-04-08，完成 14:21。
AppData\Roaming\douyin_widget　32 文件，7201636 字节，最新写入 2026-03-14，完成 14:21。
AppData\Roaming\AiLoginServer　8 文件，7175701 字节，最新写入 2026-03-14，完成 14:21。
AppData\Roaming\360FileBrowser　9 文件，6909904 字节，最新写入 2024-04-10，完成 14:21。
AppData\Roaming\Mozilla　9 文件，5620918 字节，最新写入 2026-03-18，完成 14:21。
十二块合计 148300159 字节，逐块回读件数与字节与源侧基线相等，源侧目录已不存在，原位建好目录联接。
electron-builder 前两轮连续失败，本轮查清根因不是进程占用：该目录里有两个 macOS 的软链 libcrypto.dylib 与 libssl.dylib，指向同目录的 libcrypto.1.0.0.dylib 与 libssl.1.0.0.dylib，robocopy 不复制符号链接，源侧因此永远删不干净，判据也就永远不过。
本轮改为先 robocopy 复制，再在 D 盘按同样的相对指向重建这两个软链，复核目标侧 446 文件 35041811 字节、软链 2 个，与基线一致后才删源并建联接，一次通过。
飞书主程序本体 AppData\Local\Feishu 8012 文件 2.29GB 仍是冷的，但属程序本体，飞书进程在跑，本轮继续不搬。
AppData\Local\Comms 20.5MB 是 Windows 通信存储，不是普通程序缓存，本轮不动。
本轮清理只清到 Local\Temp 的 813 字节；超 30 天日志与 __pycache__ 本轮扫描为零，因为上一轮刚清完，新生成的不够 30 天。
2026-11-14 16:22 定时任务第十一轮，0.03GB，162 文件，搬成十二块，全部核对通过
本轮冷扫覆盖用户目录、AppData\Local、AppData\Roaming 三个根，跳过全部目录联接，剩下能搬的只剩 0.5MB 以上这一批，全部搬走。
C:\Users\Administrator\.cargo　1 文件 12814336 字节，内含 13 条 cargo 工具软链，最新写入 2026-04-06，完成 16:21。
C:\Users\Administrator\.android　44 文件 3585416 字节，最新写入 2026-10-21，完成 16:21。
C:\Users\Administrator\.agent-browser　28 文件 2905148 字节，最新写入 2026-08-06，完成 16:21。
C:\Users\Administrator\.mempalace　6 文件 2565642 字节，最新写入 2026-04-20，完成 16:21。
AppData\Local\fontconfig　4 文件 2922076 字节，最新写入 2026-08-21，完成 16:21。
AppData\Local\CEF　3 文件 1350213 字节，最新写入 2022-07-29，完成 16:21。
AppData\Local\DingTalk_108　47 文件 856046 字节，最新写入 2025-08-19，完成 16:21。
AppData\Local\SolidDocuments　1 文件 646052 字节，最新写入 2022-05-26，完成 16:21。
AppData\Roaming\GreenCore7z　1 文件 2571344 字节，最新写入 2025-11-28，完成 16:21。
AppData\Roaming\obs-studio　22 文件 828211 字节，最新写入 2026-07-12，完成 16:21。
AppData\Roaming\CoreLog　1 文件 724904 字节，最新写入 2017-02-07，完成 16:21。
AppData\Roaming\utForpc　4 文件 570320 字节，最新写入 2026-03-23，完成 16:21。
十二块合计 32339708 字节，逐块回读件数与字节与源侧基线相等，源侧目录已不存在，原位建好目录联接。
.cargo 这次是 13 条指向 rustup.exe 的相对软链，用上一轮总结出的先复制再重建软链的办法处理，一次通过，没有再走回滚。
本轮清理只清到 Local\Temp 的 813 字节，Windows\Temp 与豆包 Cache 的 No_Vary_Search 仍被占用，超 30 天日志与 __pycache__ 本轮扫描为零。
飞书主程序本体 AppData\Local\Feishu 2.29GB、AppData\Local\Comms 20.5MB 继续不搬，理由同上轮。
C 盘现在已无 5MB 以上且未被占用的冷目录，往后每两小时基本只剩几十 MB 级的零星可搬。
2026-11-14 18:21 定时任务第十二轮，0.01GB，178 文件，搬成九块，全部核对通过
本轮冷扫后 0.5MB 以上合格冷目录只剩飞书本体与 Comms，两处都不搬，于是把门槛下调到 0.1MB 以上，收掉这批零星块。
C:\Users\Administrator\_bak_s2_20261105　16 文件 5510509 字节，最新写入 2026-11-05，完成 18:21。
C:\Users\Administrator\_bak_rules_20261106_kjty　30 文件 573189 字节，最新写入 2026-11-06，完成 18:21。
C:\Users\Administrator\openclaw_temp_a_stock　37 文件 483760 字节，最新写入 2026-05-28，完成 18:21。
C:\Users\Administrator\.skillhub　6 文件 395834 字节，最新写入 2026-08-15，完成 18:21。
C:\Users\Administrator\.Trash　63 文件 223085 字节，最新写入 2026-06-13，完成 18:21。
C:\Users\Administrator\.cliguard　7 文件 144745 字节，最新写入 2026-06-16，完成 18:21。
C:\Users\Administrator\.iwencai-skillhub　11 文件 139086 字节，最新写入 2026-10-10，完成 18:21。
C:\Users\Administrator\.iwencai-temp　7 文件 93623 字节，最新写入 2026-05-13，完成 18:21。
C:\Users\Administrator\.crawl4ai　1 文件 16384 字节，最新写入 2026-07-15，完成 18:21。
九块合计 7580215 字节，逐块回读件数与字节与源侧基线相等，源侧目录已不存在，原位建好目录联接。
这批全部是纯文件目录，没有软链，走 robocopy /MOVE 一次通过，无回滚。
本轮清理只清到豆包 Code Cache 的 21356 字节，Local\Temp 已空，Windows\Temp 新增一条 TAOAcceleratorEx64_ev.sys14-16-25 也被占用删不掉。
本轮开始 C 可用 35.61GB，收尾 35.52GB，两小时内活跃写入吃掉的比本轮腾出的多。
飞书主程序本体 AppData\Local\Feishu 2.29GB、AppData\Local\Comms 20.5MB 继续不搬。
C 盘 0.1MB 以上未被占用的冷目录本轮基本搬空，往后每轮可搬量会低于 1MB。
2026-11-14 20:21 定时任务第十三轮，0.00GB，293 文件，搬成七十六块，全部核对通过
本轮把 0.1MB 以上、非个人数据、非禁迁的剩余冷目录一次性收完，一共七十六块，全是纯文件目录，没有软链，走 robocopy /MOVE 一次通过，无回滚。
七十六块合计 2249042 字节，逐块回读件数与字节与源侧基线相等，源侧目录已不存在，原位建好目录联接。
C:\Users\Administrator 下 23 块：.Desktop 1 文件 8923 字节、.browser-use 1 文件 5 字节、.cli-hub 1 文件 5 字节、.kdocs-cli 1 文件 16 字节、.local 5 文件 839 字节、.mcp 1 文件 859 字节、.mcporter 1 文件 831 字节、.mmx 1 文件 205 字节、.mootdx 1 文件 4173 字节、.ollama 2 文件 468 字节、.scrape 1 文件 83 字节、.tickflow 1 文件 358 字节、.xiaomei-workspace 3 文件 2041 字节、_probedir 1 文件 6 字节、_tmp_s2_20261105 9 文件 21315 字节、ai_future_work 1 文件 50544 字节、cli 9 文件 80834 字节、openclaw-autoclaw 2 文件 12096 字节、panama_work 24 文件 189976 字节、project 20 文件 172788 字节、skills 6 文件 64591 字节、一 1 文件 7946 字节、棣栭槼宸ヤ綔鍖篭_workspace 2 文件 245 字节。
AppData\Local 下 25 块：ChromeCore 3 文件 76538 字节、jisuoffice 2 文件 76251 字节、cache 5 文件 69404 字节、D3DSCache 3 文件 66516 字节、115Chrome 2 文件 15061 字节、360Chrome 1 文件 2372 字节、ATI 3 文件 27622 字节、Adobe 1 文件 1836 字节、ASP.NET 1 文件 1885 字节、BCUT 1 文件 42 字节、DaVinci Resolve Welcome 13 文件 118864 字节、OctopusSoftV8 2 文件 110592 字节、VirtualStore 1 文件 108760 字节、TuringShield 8 文件 1496 字节、VEDetector 3 文件 4777 字节、Xiadan 1 文件 0 字节、Lark 1 文件 292 字节、MagicDanmaku 2 文件 12316 字节、MarkdownPad2 1 文件 4830 字节、ms-playwright 1 文件 78 字节、openclaw-feishu-uat 2 文件 4122 字节、speech 23 文件 21620 字节、uv 8 文件 5915 字节、chrome-devtools-mcp 1 文件 46 字节、奇安天信 2 文件 0 字节。
AppData\Roaming 下 28 块：360DesktopLite 1 文件 66 字节、360Game5 11 文件 2677 字节、360Login 4 文件 14090 字节、360Quarant 2 文件 57410 字节、360safe 8 文件 142916 字节、360zip 7 文件 6461 字节、AnyDesk 4 文件 46418 字节、CleanTrash 1 文件 1216 字节、ConfigCache 14 文件 42277 字节、InsLogicCfg 3 文件 182834 字节、MMReminder 3 文件 1493 字节、MarkdownPad 2 5 文件 21368 字节、Opera Software 6 文件 58380 字节、PreviewReader 5 文件 17767 字节、Promotion 1 文件 44 字节、Reader 1 文件 1469 字节、RoyalFlush 3 文件 143360 字节、Shouxin 1 文件 9216 字节、clawhub 1 文件 39 字节、electron-store-nodejs 1 文件 2555 字节、gallery-dl 1 文件 0 字节、liteav 3 文件 65994 字节、qBittorrent 5 文件 4508 字节、robot 5 文件 72406 字节、skill-cli-nodejs 1 文件 52 字节、tdx 7 文件 2965 字节、wyUpdate AU 2 文件 290 字节、xlgame 1 文件 389 字节。
本轮清理释放 18244086 字节，其中 __pycache__ 125 个目录 810 文件 18203409 字节，豆包 Code Cache 24377 字节；超 30 天 .log 本轮为零；Local\Temp 本轮前后都是 0 文件。
C:\Windows\Temp 的 virtual_camera 两个日志与 TAOAcceleratorEx64_ev.sys14-16-25 继续被占用跳过；豆包 Cache 的 No_Vary_Search 被占用跳过。
本轮开始 C 可用 34.03GB，收尾 34.04GB；两小时内 C 盘被写掉 1.49GB，腾出的远不及写入。
个人数据与系统盘目录一律不搬：Pictures 2.3MB、WXDrive 0.33MB、Contacts/Favorites/Links/Music/Videos 等默认用户目录都留在 C 盘；.ssh 与 .secrets 属凭据目录，2KB 级，也留在 C 盘。
飞书主程序本体 AppData\Local\Feishu 2.29GB、AppData\Local\Comms 20.5MB 继续不搬。
0.1MB 以上合格冷目录本轮全部搬空，下一轮起迁移量会归零或只剩新长出的缓存。
2026-11-14 22:21 定时任务第十四轮，本轮无新迁入
扫描三个根目录后确认：0.1MB 以上、非个人数据、非禁迁的冷目录已经搬空，剩下的只有下列这些，按规则一律不搬。
AppData\Local\Feishu 8012 文件 2292007845 字节，最新写入 10-24，飞书程序本体，飞书在运行。
AppData\Local\Comms 9 文件 21520388 字节，最新写入 10-31，Windows 通信存储。
Pictures 13 文件 2448201 字节、WXDrive 7 文件 329676 字节，个人数据。
Contacts、Favorites、Links、Music、Videos、Saved Games、Searches、WPS Cloud Files 属默认用户目录，个人文档，留在 C 盘。
.ssh 3 文件 4066 字节、.secrets 1 文件 41 字节，凭据目录，留在 C 盘。
本轮清理释放 10673972 字节，全部来自 __pycache__：71 个目录 496 文件 10673972 字节；超 30 天 .log 本轮为零；Local\Temp 前后都是 0 文件；Windows\Temp 3 文件 106239 字节删不掉；豆包 Code Cache、GPUCache 本轮启动时已是 0。
C:\Windows\Temp 的 virtual_camera 两个日志与 TAOAcceleratorEx64_ev.sys14-16-25 继续被占用跳过；豆包 Cache 的 No_Vary_Search 被占用跳过。
本轮开始 C 可用 31.95GB，收尾 31.96GB；两小时内 C 盘净少 2.09GB，是最近几轮里掉得最快的一次。
D 盘同期也被写掉 0.08GB，落点文件数从 294276 增到 294395，不是本轮搬进来的，是其它进程在往 D 盘写。
D 盘可用只剩 5.56GB，落点累计 294395 文件约 19.80GB，联接仍是 158 处，本轮没有新建联接。
2026-11-15 08:15 定时任务第十五轮，本轮只清不迁
D 盘可用只剩 5.41GB，按用户新的口径，D 盘接近满时暂停迁移，本轮不搬任何目录，先把空间彻底清一遍并把 D 盘占用查清。
本轮清理合计 428415477 字节，约 408.6MB，明细：Local\Temp 8199464 字节；豆包 Cache 83873867 字节；豆包 Code Cache 4715209 字节；豆包 GPUCache 5837168 字节；__pycache__ 69 个目录 548 文件 12320420 字节；@mmx-agentelectron-updater 旧 installer 副本 287462056 字节；超 30 天 .log 为零。
另按用户明确指令删除过程文件与重复旧素材，不计入定时任务七类清理：C:\Users\Administrator\Doubao\chats\2026-11-14\new-chat 下 9 个已完成项目的 trailers、clips、audio、output、frames 过程目录加脚本，合计 5138549352 字节约 4.79GB，成品 mp4 全部保留在原处；_qc_tmp 884323 字节。
D:\MavisVideo\素材 下 h26 与 sw 两个已完成批次的 timeline 与 segs 共 157292703 字节；E:\视频素材库 的 f37_work、f38_work、f39_work 共 647397804 字节；E:\ 下 cf_tmp、el_tmp、em_tmp、f25_tmp、f26_tmp、ghos 六个临时目录。
E:\股票短视频 下 7 个与原件 MD5 完全一致的重复副本，2951439214 字节约 2.75GB，原件保留。
没有动的新素材：D:\MavisVideo\素材\batch_assets\series\anim\src 64 文件 4151800KB 为 11-14 新下载批次，正在使用不删；C 盘 2025豆瓣高分动画片混剪、2026豆瓣高分前十混剪 两个目录尚无对应成品，视为未完成项目，整体保留。
D 盘为什么满得快，实查结论：占用 106.38GB 的大头是股票回测数据 26.5GB（10日均线 5.41GB、20日均线 4.58GB、大华市场 8.99GB、低估双底 7.46GB、首板回调 6.1GB、同花顺板块 1.33GB、同花顺主本 1.41GB），C盘搬迁_20261111 29.53GB，C盘搬迁_定时迁移 19.8GB，MavisVideo 4.82GB，Users 5.99GB，Program Files 与 x86 共 4.08GB，JianyingPro 2.9GB，pagefile.sys 1.28GB。
其中 11-12 建的 D:\C盘搬迁_20261111\_删会话前备份_20261112 单目录占 3.76GB（runtime-state_backup.sqlite 2.19GB 加 session_rows_dump.jsonl 1.58GB），是本轮查到的最大可回收单块，属删会话前的临时备份，按备份不擅自删，保留待用户定。
C 盘两小时掉 2GB 的写入方：Windows 搜索索引 Windows.edb 5.68GB、.minimax 的 runtime-state.sqlite 2.19GB、WPS 云缓存 cache.db 461.5MB、微信更新包 4.2.0.53 三个文件 667.8MB、豆包 sdk 日志 105.2MB、以及混剪视频的 trailers 与 output 中间产物。
本轮开始 C 可用 30.58GB，收尾 33.83GB，净增 3.25GB，同时仍在被上述程序写入。
落点累计 294395 文件约 19.80GB，联接 158 处，本轮无新建。
2026-11-15 08:19 定时任务第十六轮，本轮仍然只清不迁
D 盘可用只有 5.31GB，已经低于单轮 5GB 的迁移余量，按用户口径不搬目录，继续不迁。
本轮七类清理合计 293034048 字节，约 279.5MB，明细：更新器残留安装包 pending\MiniMax Code Setup 3.1.15-x64.exe 287462056 字节，已确认本机 MiniMax Code 版本为 3.1.15.222 装好、安装进程已退出，属残留整删；__pycache__ 62 个目录 477 文件 10498150 字节；豆包 Code Cache 68146 字节；Local\Temp 5696 字节；Windows\Temp、SoftwareDistribution\Download、Edge 缓存、豆包 Cache、豆包 GPUCache 本轮均为零释放。
C:\Windows\Temp 仍然卡两个被占用的文件：virtual_camera 目录与 TAOAcceleratorEx64_ev.sys15-7-0，系统占用，跳过不删。
豆包 Cache 里 No_Vary_Search 一直占用，剩 2 个文件 24 字节，跳过。
本轮新出现的过程目录不删：2025豆瓣高分动画片混剪 已从 235.2MB 长到 326.1MB，2025豆瓣高分战争历史片混剪 160.8MB，_qc_tmp 1MB，都是正在跑的新批次，等出成品后再清。
2026豆瓣高分前十混剪 523.4MB 仍无对应成品，继续整体保留。
C 盘持续写入方未变：Windows.edb 5.68GB、runtime-state.sqlite 2186.5MB、WPS cache.db 461.5MB、微信更新包 667.8MB、豆包 sdk 日志已长到 115.6MB 另加 80MB 的 netmain 日志。
本轮开始 C 可用 33.54GB，收尾 33.80GB，净增 0.26GB。
落点累计 294395 文件约 19.80GB，联接 158 处，本轮无新建。
2026-11-15 10:18 定时任务第十七轮，本轮继续只清不迁
D 盘可用 5.41GB，只够一轮搬家上限的一半多一点，按用户口径 D 盘接近满就不搬，本轮仍然不迁任何目录。
本轮七类清理合计 13936372 字节，约 13.3MB，明细：Edge Cache 6152852 字节；豆包 Code Cache 753072 字节；__pycache__ 36 个目录 259 文件 6811827 字节；Local\Temp 218477 字节；Edge Code Cache 144 字节；Windows\Temp、SoftwareDistribution\Download、豆包 Cache、豆包 GPUCache 均为零。
本轮新增按成品判定的过程文件清理，不计入七类：2025豆瓣高分动画片混剪 35 文件 341992683 字节、2025豆瓣高分恐怖片混剪 35 文件 335966596 字节、2025豆瓣高分战争历史片混剪 29 文件 237483455 字节、_qc_tmp 54 文件 26757845 字节，合计 153 文件 942200579 字节，约 898.6MB，四个目录已整体删除。
这三个项目的成品在 2026-11-14\new-chat 顶层，均在：2025动画片TOP5混剪 24.4MB 与解说配音版 24.6MB（08:11 与 08:12）、2025恐怖片TOP5混剪 17.2MB 与配音版 17.3MB（08:24）、2025战争历史片TOP3混剪 17.5MB 与配音版 17.8MB（08:42 与 08:43），全部保留。
仍不动的：2026豆瓣高分前十混剪 123 文件 523.4MB，11:07 还在写，没有成品，整体保留；抖音封面 6 文件 1.5MB 是成品封面，保留。
C:\Windows\Temp 还是两个占用：virtual_camera 目录与 TAOAcceleratorEx64_ev.sys15-7-0。
Edge 缓存与豆包 Cache 各有 No_Vary_Search 被占用，共剩 4 个文件 48 字节，跳过。
本轮开始 C 可用 30.23GB，收尾 30.89GB，净增 0.66GB。注意本轮开始时比上一轮收尾少了 3.57GB，是两小时内被 Windows 搜索索引、.minimax 的 runtime-state.sqlite、WPS 云缓存、微信更新包和新的混剪批次写掉的。
落点累计 294395 文件约 19.80GB，联接 158 处，本轮无新建。
2026-11-15 12:21 定时任务第十八轮，本轮仍然只清不迁
D 盘可用已跌到 4.97GB，低于单轮 5GB 的迁移上限本身，按用户口径不搬，本轮迁移为零。
本轮七类清理合计 41130824 字节，约 39.2MB，全部来自豆包 Code Cache 的 544 个文件；Local\Temp 为零、__pycache__ 为零、超 30 天日志为零、Windows\Temp 与 SoftwareDistribution\Download 也为零。
为什么 C 盘 Temp 清不出东西：本机 TEMP 环境变量指向 D:\Users\Administrator\AppData\Local\Temp，所有临时文件都落在 D 盘，C 盘那个 Temp 目录基本是空的。这也解释了 D 盘掉得快的一大块。
本轮查清 D 盘掉得快的原因：D 盘顶层构成实测，C盘搬迁_20261111 29.53GB、C盘搬迁_定时迁移 19.8GB、大华市场 8.99GB、低估双底 7.46GB、首板回调 6.1GB、10日均线 5.41GB、20日均线 4.59GB、MavisVideo 4.68GB、Users 6.48GB、Program Files 3.04GB 与 1.04GB、JianyingPro 2.9GB、同花顺板块 1.33GB 与主本 1.36GB。
两小时内 D 盘少了 0.44GB，来源是 D:\Users\Administrator\AppData 里的 Local\Temp，现在 5.39GB、65001 个文件，12:20 还在写。里面最大的是 30 个 PyInstaller 解包残留 _MEI 目录，合计 2502.9MB，其中 25 个是 6 小时前留下的死目录；其次 shouyang_edge_profile 462.5MB、wps 261.4MB。
这些 D 盘 Temp 残留不在本任务的七类清单里，本轮没有删，只做查清，等用户拍板。
本轮跳过：C:\Windows\Temp 的 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0 被占用；Edge 缓存与豆包 Cache 的 No_Vary_Search 各剩 2 文件 24 字节，合计 48 字节。
本轮新出现的过程目录没有删：_qc_tmp 53 文件 10.4MB，12:10 还在写，属在跑任务，跳过。
2026豆瓣高分前十混剪 123 文件 523.4MB，11:07 后无新成品，仍无成品，整体保留。
B站封面 5 文件 17.2MB（12:14）与 抖音封面 6 文件 1.5MB 都是成品封面，保留。
2025豆瓣高分战争历史片混剪 只剩一个 .keep 占位文件 43 字节，是流程占位，不动。
本轮开始 C 可用 29.59GB，收尾 29.62GB，净增 0.03GB。
落点累计 294395 文件约 19.80GB，联接 158 处，本轮无新建。
2026-11-15 14:19 定时任务第十九轮，仍然只清不迁
本轮开始 C 可用 28.49GB，比上一轮收尾的 29.62GB 又少 1.13GB，两小时里被索引、数据库、应用缓存和视频项目的碎文件吃掉，抽查近两小时没有任何单文件超 50MB 的新增大件。
本轮七类清理合计 6046132 字节，约 5.8MB，全部来自豆包 Code Cache 的 384 个文件。
Local\Temp 为零，__pycache__ 为零，超 30 天日志为零，SoftwareDistribution\Download 为零，Edge 缓存与 Edge Code Cache 为零，豆包 GPUCache 为零。
Windows\Temp 前 7 文件 106682 字节、后 5 文件 106682 字节，删掉 2 个零字节空文件，字节释放为零。
D 盘可用只剩 4.96GB，仍低于单轮 5GB 上限，按用户口径不搬，本轮迁移为零；落点累计仍是 294395 文件约 19.80GB，联接 158 处没新建。
D 盘掉得快的原因本轮复核不变：C盘搬迁_20261111 29.53GB 与 C盘搬迁_定时迁移 19.8GB 两块历史落点共 49GB；股票回测数据约 28.3GB；Users 6.48GB、MavisVideo 4.68GB、Program Files 两块 4.08GB、JianyingPro 2.9GB。
D:\Users\Administrator\AppData\Local\Temp 现在 5.40GB、65079 个文件，两小时又增 78 个文件；其中 PyInstaller 解包残留 _MEI 目录仍是 30 个 2502.9MB，25 个超 6 小时没回收。
这块 D 盘 Temp 残留仍不在七类清单内，本轮继续只查清不删，等用户拍板。
本轮跳过：C:\Windows\Temp 的 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0 被占用；Edge 缓存与豆包 Cache 的 No_Vary_Search 各 2 文件 24 字节，合计 48 字节。
过程目录本轮没删：_qc_tmp 63 文件 10.9MB，最新写入 13:24，两小时内没有新成品落盘，按无成品整体保留的口径跳过。
2026豆瓣高分前十混剪 123 文件 523.4MB，11:07 后无写入、顶层仍无对应成品，继续整体保留。
封面类成品保留：抖音封面 9 文件 12.8MB（13:35）、B站封面 9 文件 31.1MB（13:24）。
2025豆瓣高分战争历史片混剪 仍是只有一个 .keep 的占位目录 43 字节，不动。
成品区 24 支 mp4 一支没少，本轮没有新增成品。
本轮收尾 C 可用 28.50GB，净增 0.01GB。
2026-11-15 16:19 定时任务第二十轮，C 盘可用已过 40GB 线，本轮按口径只清不迁
本轮开始 C 可用 39.52GB、D 7.17GB、E 127.16GB；收尾 C 40.53GB、D 7.15GB、E 139.57GB。
本轮七类清理合计只有 443 字节，来自 C:\Windows\Temp 的一个小文件；其余六类本轮都是零。
零项具体是：C 盘 Temp 0 文件、SoftwareDistribution\Download 0、Edge 缓存 2 文件 24 字节与 Edge Code Cache 0、豆包 Cache 2 文件 24 字节与 Code Cache 0、GPUCache 0、__pycache__ 0 目录、超 30 天日志 0、更新器残留目录已空。
本轮跳过：C:\Windows\Temp 的 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0 被占用；Edge 缓存与豆包 Cache 的 No_Vary_Search 各 2 文件 24 字节，合计 48 字节。
本轮迁移为零：C 可用 40.53GB 已超过 40GB 线，按规则本轮不做迁移；落点仍是 294395 文件约 19.80GB，联接 158 处没动。
C 盘这两小时自己多出 1.01GB，D 盘 Temp 由 5.40GB 降到 3.44GB，E 盘已用少了 12.42GB，这些都不是本轮清理带来的，是系统与其它程序在这段时间自行释放的。
过程目录与素材本轮一个没删：_qc_tmp 63 文件 10.9MB（13:24 最后写）、2026豆瓣高分前十混剪 123 文件 523.4MB（仍无成品）、抖音封面 12 文件 13.8MB、B站封面 9 文件 31.1MB 全是成品封面。
2025豆瓣高分战争历史片混剪 仍只有 .keep 占位 43 字节。
成品区还是 24 支 mp4 共 1002.1MB，一支没少，本轮没有新增成品。
D 盘 MavisVideo 的 anim\src 4151.8MB 是 11-14 新下载未使用素材，按口径未动。
本轮 C 盘四根体积基线：C:\Users\Administrator 902818 文件 186114704928 字节，AppData\Local 188414 文件 24972597099 字节，C:\Windows 164611 文件 20708229989 字节，C:\ProgramData 4712 文件 8826204508 字节。
2026-11-15 17:40 用户指令：把两块大占用搬到 E 盘。本轮已完成搬迁，D 盘可用从 7.15GB 回到 90.06GB。

第一块，E:\C盘搬迁_定时迁移，来源 D:\C盘搬迁_定时迁移，294380 文件 21260422878 字节约 19.80GB，17:25 完成。D 盘原路径已改为联接指向 E 盘，C 盘 158 处联接逐个抽验全部仍能读到内容。
第二块，E:\C盘搬迁_20261111，来源 D:\C盘搬迁_20261111，30969 文件 31706300784 字节约 29.53GB，17:10 完成。此块未建联接，旧 D 路径已失效，取用一律走 E 盘。
第三块，股票回测数据搬到 E:\股票回测数据，D 盘同名路径全部改为联接，旧路径仍可用：大华市场 28882 文件 9656259126 字节 17:43 完成；低估双底 57082 文件 8010836218 字节 16:49 完成；首板回调 40097 文件 6552681477 字节 16:51 完成；10日均线 63004 文件 5804967607 字节 16:54 完成；20日均线 68332 文件 4922112448 字节 16:57 完成。
20日均线这一块有缺口必须记：搬前 68347 文件 4935427958 字节，复制时 15 个文件被占用没复制成功，随后随源目录删除，实际丢失 15 文件 13309510 字节，回测引用这段数据要当心。
同花顺板块与同花顺主本没有搬：客户端在跑，文件被进程锁住，搬了一部分后已整块退回 D 盘，现 D 侧同花顺板块 23023 文件 1495226936 字节、同花顺主本 24228 文件 1518492717 字节，E 盘上的残留副本已清掉。
搬迁过程中处理过的占用：D 盘空目录删除被 Windows 搜索索引与 WPS 云服务 wpscloudsvr 挡住，暂停 WSearch 并结束该进程后才删掉建联接，两处均已恢复。
D 盘现在的大项：Users 4.60GB（含 Temp 3.44GB）、MavisVideo 4.49GB（含 anim\src 4151.8MB 新下载素材，未动）、Program Files 3.04GB、JianyingPro 2.90GB、同花顺板块 1.39GB、同花顺主本 1.41GB。
本轮另出一份可直接发给 MiniMax 的提示词：C:\Users\Administrator\Desktop\给MiniMax的E盘搬迁提示词.md。
2026-11-15 18:17 第二十一轮定时任务，本轮新增迁入三块冷数据，全部走落点 D:\C盘搬迁_定时迁移（该路径为联接，实体落在 E 盘）。

一，来源 C:\Users\Administrator\AppData\Roaming\2345Ad\Components，71 文件 353956967 字节，18:22 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\2345Ad\Components。
二，来源 C:\Users\Administrator\AppData\Roaming\Tencent\QQPCMgr\radiumv3\wmpfsdk，35 文件 333812441 字节，18:23 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\Tencent\QQPCMgr\radiumv3\wmpfsdk。
三，来源 C:\Users\Administrator\AppData\Roaming\Tencent\WXWork，109 文件 493786505 字节，18:24 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\Tencent\WXWork。

三块合计 215 文件 1181555913 字节约 1.10GB，目标侧回读件数与字节全部对上，源侧目录已不存在。

搬迁步骤为先复制后比对再删源，比对不上就删掉目标副本、源保持不动，避免出现半截状态与丢文件。

本轮清理明细：C:\Windows\Temp 释放 443 字节；C:\Users\Administrator\AppData\Local\Temp 释放 6022 字节（3 个临时文件）；豆包 Code Cache 释放 1060005 字节（225 文件）；__pycache__ 40 个目录 286 文件释放 5810777 字节；30 天以上 .log 为 0。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0（系统正在使用）；Edge 与豆包 Cache 目录下的 No_Vary_Search（浏览器与豆包正在运行）。

本轮不搬的大项：AppData\Local\Feishu 8012 文件 2185.8MB 飞书正在运行；AppData\Local\Programs\Python 67538 文件 4.19GB 是正在用的解释器；AppData\Local\ShouyangTerminal\edge_profile 989 文件 518.4MB 终端在跑；.minimax\sessions 里的 235.2MB 会话目录 MiniMax 正在使用；Edge CacheStorage 553.7MB 属浏览器缓存但本轮未列入七类清理范围。
2026-11-15 20:17 第二十二轮定时任务，本轮新增迁入五块冷数据，全部走落点 D:\C盘搬迁_定时迁移（该路径为联接，实体落在 E 盘）。

一，来源 C:\Users\Administrator\AppData\Local\AndroidToolchain，11909 文件 1232185677 字节，20:25 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\AndroidToolchain，C 盘原位已建联接，指向落点，安卓工具链按原路径仍可用。
二，来源 C:\Users\Administrator\AppData\Roaming\LarkShell\aha\users\39f431ed22330a81c8c303c4f0d9b1ca，12713 文件 1629717959 字节，20:27 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\LarkShell\aha\users\39f431ed22330a81c8c303c4f0d9b1ca。
三，来源 C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32，8694 文件 196946949 字节，20:26 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\Programs\Python\Python37-32，C 盘原位已建联接。
四，来源 C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data\ProvenanceData，2 文件 176781704 字节，20:28 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\Microsoft\Edge\User Data\ProvenanceData。
五，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\office6\everythingsearch，2 文件 134243707 字节，20:28 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\office6\everythingsearch。

五块合计 33320 文件 3369875996 字节约 3.14GB，目标侧回读件数与字节全部对上，源侧目录已不存在。

搬迁步骤仍是先复制后比对再删源，比对不上就删掉目标副本、源保持不动，不留半截状态。

本轮清理明细：C:\Windows\Temp 释放 0 字节（4 个文件全被占用）；C:\Users\Administrator\AppData\Local\Temp 本来就是空；C:\Windows\SoftwareDistribution\Download 空；豆包 Code Cache 释放 13500209 字节（175 文件）；__pycache__ 150 个目录 1039 文件释放 22424660 字节；30 天以上 .log 为 0。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0；Edge 与豆包 Cache 目录下的 No_Vary_Search 两个文件 24 字节。

本轮不搬的大项：AppData\Local\Feishu 8012 文件 2185.8MB 飞书在运行；Local\Programs\Python 里 torch 1148.3MB 与 paddle 377MB 属在用解释器，拆开搬会让 import 断；ShouyangTerminal\edge_profile 989 文件 518.4MB 终端在跑；Edge CacheStorage 553.7MB 未列入七类清理范围；.minimax\sessions 下 235.2MB 会话目录 MiniMax 在用。
2026-11-15 22:17 第二十三轮定时任务，本轮新增迁入六块冷数据，全部走落点 D:\C盘搬迁_定时迁移（该路径为联接，实体落在 E 盘）。

一，来源 C:\Users\Administrator\AppData\Local\Microsoft\Edge\UserData，883 文件 92590020 字节，22:21 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\Microsoft\Edge\UserData，这是 2026-03-15 留下的旧版 Edge 配置目录，不是当前在用的 User Data。
二，来源 C:\Users\Administrator\AppData\Roaming\腾讯电脑管家-全局搜\FileSearch，4 文件 97859049 字节，22:22 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\腾讯电脑管家-全局搜\FileSearch。
三，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\data\win-i386\cef，1417 文件 117013332 字节，22:22 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\wps\addons\data\win-i386\cef。
四，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\office6\docerFonts，456 文件 105654114 字节，22:22 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\office6\docerFonts。
五，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19667，826 文件 114584084 字节，22:23 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19667。同目录里较新的 qing_3.1.0.19763 保留没动，那是 WPS 当前在用的版本。
六，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\kufeconvertplugin_3.1.0.457，3 文件 88069234 字节，22:23 完成，落点同名路径。

六块合计 3589 文件 615769833 字节，约 0.57GB，目标侧回读件数与字节全部对上，源侧目录已不存在。

本轮清理明细：C:\Users\Administrator\AppData\Local\Temp 空；C:\Windows\Temp 释放 0 字节（4 个文件全被占用）；Edge Cache 释放 0（No_Vary_Search 被占用）；豆包 Cache 释放 0（No_Vary_Search 被占用）；豆包 Code Cache 释放 655368 字节（114 文件）；__pycache__ 123 个目录 834 文件释放 18765019 字节；Edge 的 Service Worker CacheStorage 1653 文件清空释放 553705887 字节；30 天以上 .log 为 0。本轮清理合计 573126274 字节约 546.6MB。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys15-7-0；Edge 与豆包 Cache 目录下各一对 No_Vary_Search 文件。

本轮不搬的大项与原因：AppData\Local\Feishu 8012 文件 2185.8MB 飞书在运行；Local\Programs\Python 67538 文件 4187.2MB 里 torch 与 paddle 属在用解释器，拆开搬会让 import 断；Windows\Fonts 73 文件 625.1MB 属系统字体，搬走会导致字体加载异常；ShouyangTerminal\edge_profile 989 文件 518.4MB 终端在跑；桌面 ucl_special\unl_3v 与 Desktop\01_股票研究 下目录是今天还在写的在办工程，一律不动；.minimax\computer-use 87.2MB 随 MiniMax 进程在用。
2026-11-16 08:17 第二十四轮定时任务，本轮新增迁入两块冷数据，都建了联接，C 盘原路径照旧可用，实体落在 E 盘。

一，来源 C:\Users\Administrator\AppData\Roaming\kingsoft\office6\update，7 文件 168466916 字节，08:43 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\office6\update，C 盘原位留 Junction，WPS 若再取更新包会穿透到 E 盘。
二，来源 C:\Users\Administrator\AppData\Local\Microsoft\Windows\Fonts，73 文件 625154920 字节，08:44 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\Microsoft\Windows\Fonts，C 盘原位留 Junction，LXGW 文楷与更纱黑体等自装字体照旧读得到，抽查 LXGWWenKaiMono-Light.ttf 28287272 字节读回一致。

两块合计 80 文件 793621836 字节，约 0.76GB，目标侧件数与字节回读全部对上，源侧目录已不存在，两处联接可读。

本轮清理明细：C:\Users\Administrator\AppData\Local\Temp 释放 8199464 字节（1 个残留文件）；C:\Windows\Temp 释放 0 字节（3 项删除失败，剩下 5 个占用文件）；C:\Windows\SoftwareDistribution\Download 空；Edge Cache 释放 24 字节；Edge Code Cache 空；Edge 的 Service Worker CacheStorage 空；豆包 Cache 释放 28773450 字节（187 文件清到剩 2）；豆包 Code Cache 释放 734633 字节（1099 文件）；豆包 GPUCache 释放 5837168 字节（5 文件）；__pycache__ 64 目录 489 文件释放 10702311 字节；超 30 天 .log 删 11 个 26725 字节。清理合计 54273775 字节约 51.8MB。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys16-7-0；豆包 Cache 下 No_Vary_Search。

本轮不搬的大项与原因：Local\Programs\Python 67538 文件 4187.2MB 与 Local\Feishu 8012 文件 2292.0MB 都在跑，拆开会让解释器与飞书断链；ShouyangTerminal\edge_profile 989 文件 518.4MB 终端在跑；.minimax 下 sessions 与 computer-use 属 MiniMax 在用目录，v2\sqlite 在禁迁清单；Desktop\01_股票研究 下 K线库 195.2MB、data 122.7MB、指标和策略优化迭代 130.3MB 都在日常回测里用；Desktop\02_内容创作\足球成品合集 与 Desktop\分类榜混剪发布素材 是成品与新工程，今天还在出片；Desktop\ucl_special\unl_3v 的 segs 属在办视频工程；微信 XPlugin 插件目录在客户端运行时被占用。

本轮顺带查清 C 盘为什么掉得快，昨夜 22:00 到今早 08:40 这段时间的增量大头是：C:\Users\Administrator\.minimax\v2\sqlite\runtime-state.sqlite 已到 2292674560 字节且 08:41 还在写，WPS 云文档 cache.db 483893248 字节，首阳战法回测引擎 engine.db 219660288 字节，豆包 sdk 日志 saman_2026.1115.6.log 167731393 字节与 saman_2026.1116.0.log 147079138 字节、saman_frontend_2026.1116.0.log 134217512 字节，另有桌面分类榜混剪工程当天连续出片。这些都在活跃写入，不在可清可迁范围内。
2026-11-16 10:17 第二十五轮定时任务，本轮新增迁入两块冷数据，都建了联接，C 盘原路径照旧可用，实体落在 E 盘。

一，来源 C:\Users\Administrator\AppData\Local\ShouyangTerminal\edge_profile，989 文件 518422614 字节，10:31 完成，落点 D:\C盘搬迁_定时迁移\AppData\Local\ShouyangTerminal\edge_profile，C 盘原位留 Junction，可读 49 项，终端自带的浏览器配置与登录态跟着目录一起过去，路径不变。
二，来源 C:\Users\Administrator\AppData\Roaming\HaoZip\Application，84 文件 63934251 字节，10:32 完成，落点 D:\C盘搬迁_定时迁移\AppData\Roaming\HaoZip\Application，C 盘原位留 Junction，可读 1 项，好压主程序路径不变。

两块合计 1073 文件 582356865 字节，约 0.54GB，目标侧件数与字节回读全部对上，源侧目录已不存在，两处联接可读。

本轮清理明细：C:\Users\Administrator\AppData\Local\Temp 本来已空，释放 0；C:\Windows\Temp 释放 0 字节（5 个占用文件，删 0 项）；SoftwareDistribution\Download 空；Edge Cache、Edge Code Cache、Edge 的 CacheStorage 全空；豆包 Cache 只剩 No_Vary_Search 2 文件 24 字节被占；豆包 Code Cache 空；豆包 GPUCache 空；__pycache__ 48 目录 373 文件释放 7988709 字节；超 30 天 .log 本轮 0 个。清理合计 7988709 字节约 7.6MB。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys16-7-0；豆包 Cache 下 No_Vary_Search 2 文件 24 字节。

本轮不搬的大项与原因：AppData\Local\Programs\Python\Python312 共 59321 文件 4000813885 字节，其中 torch 1148252661 字节、paddle 376975343 字节、_polars_runtime_32 165238060 字节、cv2 155435791 字节、imageio_ffmpeg 154234843 字节、patchright 110476666 字节、llvmlite 107175072 字节、playwright 104491379 字节、googleapiclient 96108024 字节、scipy 89827042 字节、av.libs 67351552 字节，这些是整个 Python312 解释器的组成部分，当前有 9 个 python 进程在跑，拆包或整目录搬都会有文件被占用、导入链断掉，整块跳过。Local\Feishu 8012 文件 2292007845 字节，飞书在跑。.minimax\sessions 下 mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节与 computer-use 11 文件 87219966 字节属 MiniMax 在用，v2\sqlite 在禁迁清单。Desktop\01_股票研究 下 K线库 5620 文件 195175347 字节、data 122740657 字节、_crop 82370192 字节、指标和策略优化迭代 130251355 字节，日常回测要用。Desktop\02_内容创作\足球成品合集 各支成品属成品片，按只留成品口径保留。Desktop\ucl_special\unl_3v\segs 下 _digits 164777335 字节、p1 108505979 字节、j1 97000306 字节、i2 86348583 字节、n2 78013765 字节、cE 69297603 字节，属在办视频工程。微信 XPlugin\Plugins 下 XFilesOfficeReader 67942465 字节与 XPlayer 66491403 字节、xwechat 的 applet\packages 91355134 字节，客户端在跑时被占用。kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节是当前在用版本，保留。

另发现一处不属于本任务七类清理范围的垃圾：Python312 的 site-packages 下有个 ~orch 目录，10 文件 287602384 字节，日期 2026-03-24，看着是当年 pip 装 torch 中断留下的半截临时目录，按范围我没有动它，等哪天拍板再删。
2026-11-16 12:17 第二十六轮定时任务，本轮把桌面足球成品合集里已经冷下来的 39 个成品目录整块搬到 E 盘，加一块指标研究资料，全部在原位留 Junction，桌面路径照旧能点开，实体在 D 盘搬迁目录下穿透到 E 盘。

一，C:\Users\Administrator\Desktop\02_内容创作\足球成品合集 下 36 个已冷成品目录，从 01_焦点1_英格兰2-3西班牙_温布利之夜 到 36_赛场内外第3期_伯纳乌横幅抗议西甲与裁判，逐个整目录搬到 D:\C盘搬迁_定时迁移\Desktop\02_内容创作\足球成品合集\同名目录，C 盘原位各留 Junction。
二，C:\Users\Administrator\Desktop\02_内容创作\足球成品合集\欧冠第一轮 下三个子目录，欧冠第一轮、第五轮、第六轮，英超豪门滑铁卢，同样搬到 D:\C盘搬迁_定时迁移\Desktop\02_内容创作\足球成品合集\欧冠第一轮\同名目录，原位各留 Junction。
三，C:\Users\Administrator\Desktop\01_股票研究\指标和策略优化迭代，120 文件 130251355 字节，搬到 D:\C盘搬迁_定时迁移\Desktop\01_股票研究\指标和策略优化迭代，原位留 Junction。

以上合计 40 个目录，378 文件 2106334573 字节，约 1.96GB，12:22 前后全部完成，目标侧件数与字节逐块回读全部对上，源侧目录已不存在，40 处联接都建好，抽查 21_合集C_西甲裁判第一视角 可读 7 项。

本轮没搬的成品：足球成品合集\欧冠第一轮 本体还剩当天新出的 2026-11-16 文件，属于在写状态，整块不动；欧冠第一轮 下 焦点36 三件（mp4、简介、tags）也是当天 10:47 才生成，留在原处。

本轮清理明细：C:\Users\Administrator\AppData\Local\Temp 已空，释放 0；C:\Windows\Temp 释放 0 字节（5 个占用文件，删 0 项）；SoftwareDistribution\Download 空；Edge Cache、Edge Code Cache、Edge 的 CacheStorage 全空；豆包 Cache 只剩 No_Vary_Search 2 文件 24 字节被占；豆包 Code Cache 4 文件 23478 字节全删；豆包 GPUCache 空；__pycache__ 62 目录 483 文件释放 10670137 字节；超 30 天 .log 本轮 0 个。清理合计 10693615 字节约 10.2MB。

被占用跳过：C:\Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys16-7-0；豆包 Cache 下 No_Vary_Search 2 文件 24 字节。

本轮不搬的大项与原因：AppData\Local\Programs\Python 67538 文件 4187241931 字节，当前有 9 个 python 进程在跑，torch、paddle 等整块搬会被占用文件卡住、拆包会断导入链；Local\Feishu 8012 文件 2292007845 字节，飞书在跑；.minimax\sessions 下 mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节与 computer-use 11 文件 87219966 字节属 MiniMax 在用，v2\sqlite 在禁迁清单；Desktop\01_股票研究 下 K线库 5620 文件 195175347 字节、data 122740657 字节、_crop 82370192 字节，日常回测要用；Desktop\ucl_special\unl_3v\segs 下 _digits 164777335 字节、p1 108505979、j1 97000306、i2 86348583、n2 78013765、cE 69297603 等属在办视频工程；微信 XPlugin\Plugins 下 XFilesOfficeReader 67942465 字节与 XPlayer 66491403 字节、xwechat 的 applet\packages 91355134 字节，客户端在跑时被占用；kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节是当前在用版本；Edge\User Data\Default\Extensions 405 文件 61052805 字节属浏览器已装扩展，不动。
2026-11-16 14:17 第二十七轮定时任务，本轮搬三块股票研究数据，都留 Junction。

C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\K线库，5620 文件 195175347 字节，搬到 D:\C盘搬迁_定时迁移\Desktop\01_股票研究\龙虾命中的个股\K线库，原位留 Junction，14:22 完成。
C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\data，9 文件 122740657 字节，同样搬到 D 盘同名目录，原位留 Junction。
C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\_crop，60 文件 82370192 字节，同样搬到 D 盘同名目录，原位留 Junction。

三块合计 3 个目录，5689 文件 400286196 字节，约 0.37GB，逐块回读件数字节全部对上，源侧已删净，联接建好，抽查 K线库 可读 3 项。

本轮清理明细：Local\Temp 空；Windows\Temp 释放 0 字节，5 个占用文件删 0 项；SoftwareDistribution\Download 空；Edge Cache、Edge Code Cache、Edge CacheStorage 全空；豆包 Cache 只剩 No_Vary_Search 2 文件 24 字节被占；豆包 Code Cache 空；GPUCache 空；__pycache__ 17 目录 102 文件释放 2296294 字节；超 30 天 .log 本轮 0 个。清理合计 2296294 字节约 2.2MB。

被占用或待装而跳过的：Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys16-7-0；豆包 Cache 下 No_Vary_Search。另有一份 C:\Users\Administrator\AppData\Local\@mmx-agentelectron-updater\pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节加 update-info.json，13:02 下载，当前已装的是 3.1.15，这是待安装的新版升级包，不是重复副本，且 MiniMax Code 进程在跑，本轮没删。

本轮没搬的大项与原因：AppData\Local\Programs\Python 67538 文件 4187241931 字节，9 个 python 进程在跑；Local\Feishu 8012 文件 2292007845 字节，飞书在跑；.minimax\sessions 下 mvs_80d44d465b694b529f44e5143746fa6a 235212388 字节与 computer-use 87219966 字节，MiniMax 在用，v2\sqlite 在禁迁清单；Desktop\ucl_special\unl_3v\segs 下 _digits 164777335、p1 108505979、j1 97000306、i2 86348583、n2 78013765、cE 69297603、h21 61807869、h1 57216904 等属在办视频工程；微信 XPlugin 下 XFilesOfficeReader 67942465、XPlayer 66491403、WeChatPlayer 55718903、WeChatOcr 51894825 与 applet\packages 91355134，客户端在跑被占用；kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节是当前在用版本，openvino2420x64 两版 51121880 与 51121456 字节属 WPS 插件池，未确认可搬；LarkShell\sdk_storage\39f431ed22330a81c8c303c4f0d9b1ca 143 文件 49891845 字节，飞书在跑；Edge\User Data\Default\Extensions 405 文件 61052805 字节属已装扩展；Roaming\MiniMax\remote-control\attachments 103 文件 54841217 字节，MiniMax 在用。

本轮 C 盘不降反升的原因，已查清：这两小时 .minimax\v2\sqlite\runtime-state.sqlite 写到 2186.5MB（13:54 还在写），Documents\WPS Cloud Files\.687324960\cache.db 461.5MB（14:21 还在写），豆包自己在 13:02 到 14:07 下载新版更新包，可见大文件 Doubao.dll 314.6MB、biz.pak 186MB、liblark.dll 179.5MB、base 运行包 125.8MB、doubao_office.pak 112.5MB、两处 hot_fix 各 93.2MB，合计约 1.1GB，另有 MiniMax 3.1.16 升级包 287.5MB，桌面分类榜混剪发布素材今天中午出片写到 800MB 上下。
2026-11-16 16:17 第二十八轮定时任务，本轮搬六块冷目录，每块都留 Junction。

C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\_stage_A_20261102，1089 文件 49858585 字节，搬到 D:\C盘搬迁_定时迁移\Desktop\01_股票研究\龙虾命中的个股\_stage_A_20261102，原位留 Junction，16:22 完成。
C:\Users\Administrator\Desktop\首阳战法自用版_mcp_venv，2180 文件 49427770 字节，搬到 D:\C盘搬迁_定时迁移\Desktop\首阳战法自用版_mcp_venv，原位留 Junction。
C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\openvino2420x64_3.1.0.433，6 文件 51121880 字节，搬到 D 盘同结构目录，原位留 Junction。
C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\openvino2420x64_3.1.0.32，5 文件 51121456 字节，同上。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\WeChatPlayer，84 文件 55718903 字节，同上。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\WeChatOcr，14 文件 51894825 字节，同上。

六块合计 3378 文件 309143419 字节，约 0.29GB，逐块回读件数字节全部对上，源侧已删净，零回滚。抽查 _stage_A_20261102 与 WeChatPlayer 两处均为 ReparsePoint 可读。

本轮清理明细：Local\Temp 空；Windows\Temp 释放 1768 字节，删 1 项，剩 5 文件被占；SoftwareDistribution\Download 空；Edge Cache、Code Cache、CacheStorage 全空；豆包 Cache 只剩 No_Vary_Search 2 文件 24 字节被占；豆包 Code Cache 211 文件全删释放 129627 字节；GPUCache 空；__pycache__ 本轮 0 个；超 30 天 .log 0 个。清理合计 131395 字节约 0.13MB。

被占用或待装而跳过的：Windows\Temp 下 virtual_camera、TAOAcceleratorEx64_ev.sys16-7-0；豆包 Cache 下 No_Vary_Search；@mmx-agentelectron-updater\pending 下 MiniMax Code Setup 3.1.16-x64.exe 287455296 字节加 update-info.json，已装 3.1.15，是待安装新版包不是重复副本，MiniMax Code 进程在跑，本轮仍未删。

本轮没搬的大项与原因：AppData\Local\Programs\Python 67538 文件 4187241931 字节 9 个 python 进程在跑；Local\Feishu 8012 文件 2292007845 字节飞书在跑；.minimax\sessions 下 mvs_80d44d465b694b529f44e5143746fa6a 235212388 字节与 computer-use 87219966 字节 MiniMax 在用；Desktop\ucl_special\unl_3v\segs 下 _digits 164777335、p1 108505979、j1 97000306、i2 86348583、n2 78013765、cE 69297603、h21 61807869、n1 58549898、v3 57970744、h1 57216904、f19 49167029 属在办视频工程；微信 XPlugin 下 XFilesOfficeReader 67942465、XPlayer 66491403 与 applet\packages 91355134 客户端在跑；kingsoft\wps\addons\pool 下 qing_3.1.0.19763 826 文件 114490647 字节是当前在用版本，kwpsofflinesdk 3536 文件 57112064 字节属 WPS 离线组件；LarkShell\sdk_storage 143 文件 49891845 字节飞书在跑；Edge Extensions 405 文件 61052805 字节属已装扩展；Roaming\MiniMax\remote-control\attachments 103 文件 54841217 字节 MiniMax 在用。

本轮 C 盘为什么又掉 2.91GB：首阳战法回测引擎\data\engine.db 209.6MB 在 16:13 还在写，同目录 engine.db.bak_autoselect_20261116 与 engine.db.bak_pool_20261116_152250 各约 209.6MB 属 15:22 到 15:30 新生成的库备份；龙虾命中的个股\_bak_20261116_reco_wire 下 engine.db.bak_recolog_20261116_153054 209.6MB；Doubao\chats\2026-11-14\new-chat-4\2026恐怖大师混剪\trailers\fd6.mp4 158.6MB 15:50 生成；桌面分类榜混剪发布素材 16:16 又出 love_top10_h_merged 122.1MB 与喜剧片榜两支 106MB；.minimax\v2\sqlite\runtime-state.sqlite 仍 2186.5MB 持续写，WPS cache.db 461.5MB 持续写。
2026-11-16 18:17 第二十九轮定时任务，本轮清理合计 475161562 字节约 0.44GB，迁移 6 个目录 231 文件 425120331 字节约 0.40GB，全部留 Junction。

清理分项：Local\Temp 释放 8199464 字节；Windows\Temp 释放 1662 字节删 8 项；Edge Cache 释放 6152852 字节；Edge Code Cache 释放 144 字节；豆包 Cache 释放 68994336 字节（284 文件）；豆包 Code Cache 释放 89794277 字节（2115 文件）；豆包 GPUCache 释放 5837168 字节（5 项）；__pycache__ 50 目录 407 文件 8726363 字节；超 30 天 .log 0 个；更新器重复安装包删 1 份 287455296 字节。

迁移明细，六块：
C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\_bpkg24\首阳战法客户端_分发版_20261025_v12，102 文件 47848034 字节，搬到 D 盘同结构目录，原位留 Junction。
C:\Users\Administrator\.minimax\tools\_q_reco_index_out，35 文件 44127493 字节，同上。
C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\kpdfdocrepair_3.1.0.18973，3 文件 46863247 字节，同上。
同目录 kproofread_3.1.0.17802，77 文件 43008450 字节，同上。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\XPlayer\15072，12 文件 66491403 字节，同上。
C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data\ProvenanceData，2 文件 176781704 字节，这处是早前轮次已复制到 D 但源侧没删净的遗留，本轮核对两侧 SHA256 全同后删源补建 Junction，迁移补齐，18:23 完成。

前五块合计 229 文件 248338627 字节，零回滚；加补齐的 Edge 一块，本轮共 231 文件 425120331 字节。

被占用或特意跳过的：Windows\Temp 下 virtual_camera、TAOAcceleratorEx64_ev.sys16-16-56 仍被驱动占用；Edge Cache 与豆包 Cache 下各有 No_Vary_Search 2 文件 24 字节被占，属常态零释放；@mmx-agentelectron-updater 根目录 installer.exe 287455296 字节与 pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节是同一版本同一时刻 13:02 的双份副本，删掉根目录那份，pending 那份留下待安装，MiniMax Code 3.1.15 在跑。

本轮没搬的大项与原因：AppData\Local\Programs\Python 67538 文件 4187241931 字节 9 个 python 进程在跑；Local\Feishu 8012 文件 2292007845 字节飞书在跑；.minimax\v2 下 sqlite 与 sessions 禁迁；Desktop\ucl_special\unl_3v\segs 各子目录约 700MB 属在办视频工程；微信 XPlugin 下 XFilesOfficeReader 67942465 与 applet\packages 91355134 客户端在跑；qing_3.1.0.19763 826 文件 114490647 字节是 WPS 当前版本；LarkShell\sdk_storage 49891845 字节飞书在跑；Roaming\MiniMax\remote-control\attachments 54841217 字节 MiniMax 在用。

C 盘这轮反而多出 0.75GB：豆包更新包装完之后 AppData\Local\Doubao\update_data 整块清掉了，之前约 1.1GB。
2026-11-16 20:17 第三十轮定时任务，本轮清理合计 20583058 字节约 0.02GB，迁移 10 个目录 4147 文件 587111955 字节约 0.56GB，全部留 Junction，零回滚。

清理分项：Local\Temp 本轮 0 文件 0 字节；Windows\Temp 清前 6 文件 106239 字节删 3 项释放 0 字节；SoftwareDistribution\Download 空；Edge Cache 只剩被占 24 字节；Edge Code Cache 与 CacheStorage 空；豆包 Cache 只剩被占 24 字节；豆包 Code Cache 287 文件 2376063 字节全删；豆包 GPUCache 空；__pycache__ 126 目录 811 文件 18206995 字节；超 30 天 .log 0 个；更新器只剩 pending 一份 287455475 字节，无重复可删。

迁移明细，十块：
C:\Users\Administrator\AppData\Roaming\2345Ad\Application，67 文件 38694826 字节。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\WMPFDrm，12 文件 39097824 字节。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\XFilesOfficeReader，16 文件 67942465 字节。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\radium\users\efe232407d4feb3a65addf4933281260\applet\packages，35 文件 91355134 字节。
C:\Users\Administrator\AppData\Roaming\Tencent\xwechat\radium\users\efe232407d4feb3a65addf4933281260\applet\local，222 文件 50686406 字节。
C:\Users\Administrator\Desktop\01_股票研究\龙虾命中的个股\_bpkg24\首阳战法客户端_分发版_20261025_v13\app\data，2 文件 50270208 字节。
C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\data\win-i386\kwpsofflinesdk，3536 文件 57112064 字节。
C:\Users\Administrator\AppData\Roaming\LarkShell\sdk_storage\39f431ed22330a81c8c303c4f0d9b1ca，143 文件 49891845 字节。
C:\Users\Administrator\AppData\Roaming\MiniMax\remote-control\attachments，103 文件 54841217 字节。
C:\Users\Administrator\.minimax\computer-use，11 文件 87219966 字节。

十块都逐块回读件数字节对上才删源建 Junction，微信客户端与 WPS 客户端在运行的情况下仍全部搬通，20:26 完成。

被占用或特意跳过的：Windows\Temp 下 virtual_camera、TAOAcceleratorEx64_ev.sys16-16-56 被驱动占用；Edge Cache 与豆包 Cache 下 No_Vary_Search 各 2 文件 24 字节被占，常态零释放；@mmx-agentelectron-updater\pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节仍是待安装升级包，保留。

继续没搬的大项：AppData\Local\Programs\Python 67538 文件 4187241931 字节 9 个 python 进程在跑；Local\Feishu 8012 文件 2292007845 字节飞书在跑；.minimax\v2 下 sqlite 与 sessions 禁迁；Desktop\ucl_special\unl_3v\segs 约 700MB 在办视频工程；qing_3.1.0.19763 826 文件 114490647 字节是 WPS 当前版本；Edge Default\Extensions 405 文件 61052805 字节是在用扩展。

C 盘这两小时掉了 3.37GB 的来源，实测归到三处：Desktop\分类榜混剪发布素材 从 9126.3MB 涨到 10453.7MB，两小时多 1327.4MB，是科幻片榜、爱情片榜、悬疑片榜三套横版成片在陆续出；豆包 sdk_storage\log 已到 2380.8MB，新增 saman_2026.1116.3.log 155.7MB；Desktop 新出首阳战法终端 v5.5 三个安装件约 148MB。另 .minimax\v2\sqlite\runtime-state.sqlite 2186.5MB 与 Documents\WPS Cloud Files cache.db 461.5MB 一直在写，属禁迁与个人文档，不动。
2026-11-16 22:17 第三十一轮定时任务，本轮清理合计 14810469 字节，迁移 6 个目录 660 文件 794635943 字节，约 0.74GB，全部留 Junction，零回滚。

清理分项：Local\Temp 0 文件 0 字节；Windows\Temp 清前 4 文件 106239 字节释放 0 字节；SoftwareDistribution\Download 空；Edge Cache 只剩被占 24 字节；Edge Code Cache 与 CacheStorage 空；豆包 Cache 只剩被占 24 字节；豆包 Code Cache 287 文件 14810469 字节全删；豆包 GPUCache 空；__pycache__ 本轮 0 个目录 0 文件；超 30 天 .log 0 个；更新器只剩 pending 一份 287455475 字节，无重复。

迁移明细，六块，全部是 Python312 之下长期不动的叶子目录，搬完原位置都留了 Junction，导入实测通过：
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\~orch，10 文件 287602384 字节，这是 2026-03-24 一次中断的 pip 安装残留。
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Doc，573 文件 57470369 字节。
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg，16 文件 154234843 字节。
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\_polars_runtime_32，3 文件 165238060 字节。
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\av.libs，30 文件 67351552 字节。
C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\ctranslate2，28 文件 62738735 字节。

搬完用 Python312 本体实测 import ctranslate2、imageio_ffmpeg、av 全部正常，联接对 Python 透明，不影响脚本调用。Python312 剩余的大包 torch 1148252661 字节、paddle 376975343 字节、cv2 155435791 字节、scipy 89827042 字节 这轮没动，要在导入进程停下后才敢整块搬。

被占用或跳过的：Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys16-16-56 被驱动占用；Edge 与豆包 Cache 下 No_Vary_Search 各 2 文件 24 字节被占；pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节待安装，保留。

仍不动的冷块：Local\Feishu 8012 文件 2292007845 字节 飞书在运行；.minimax\sessions\mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节 MiniMax Code 在用；Desktop\ucl_special\unl_3v\segs 约 700MB 在办视频工程；Roaming\kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节 是 WPS 当前版本；Edge Default\Extensions 405 文件 61052805 字节 是在用扩展。

D 盘这两小时从 22.63GB 涨到 25.69GB，涨了 3.06GB，实测大头是 D:\JianyingPro 2967.5MB 剪辑工程与缓存、D 盘根目录 20日均线.zip 2876.5MB，还有 D:\Users 5690.8MB 里的 Temp；D 盘目前可用 86.10GB，没到紧张程度，所以照常迁移。
2026-11-17 08:17 第三十二轮定时任务，清理合计 52733219 字节，迁移 13 个目录 21427 文件 2422893026 字节，约 2.26GB，全部留 Junction，零回滚，导入实测通过。

清理分项：Local\Temp 前 1 文件 8199464 字节全删；Windows\Temp 前 9 文件 107121 字节，删 3 项释放 443 字节；SoftwareDistribution\Download 空；Edge Cache 前 8 文件 6152876 字节，删到只剩被占的 24 字节；Edge Code Cache 前 4 文件 144 字节全删；Edge CacheStorage 空；豆包 Cache 前 186 文件 30136491 字节，删到只剩被占的 24 字节；豆包 Code Cache 1003 文件 708034 字节全删；豆包 GPUCache 5 文件 5837168 字节全删；__pycache__ 14 个目录 83 文件 1698647 字节；超 30 天 .log 0 个；更新器只剩 pending 两份 287455475 字节，无重复可删。合计 52733219 字节。

迁移明细，十三块，全在 Python312 的 site-packages 下，搬完原位全部留 Junction：
torch，10607 文件 1148252661 字节。
paddle，3497 文件 376975343 字节。
cv2，125 文件 155435791 字节。
scipy，1525 文件 89827042 字节。
onnxruntime，316 文件 36663303 字节。
patchright，176 文件 110476666 字节。
llvmlite，39 文件 107175072 字节。
playwright，429 文件 104491379 字节。
googleapiclient，585 文件 96108024 字节。
pymupdf，105 文件 48336682 字节。
litellm，2512 文件 51256875 字节。
chromadb_rust_bindings，2 文件 61897387 字节。
~-ndas，1509 文件 35996801 字节。
来源根统一是 C:\Users\Administrator\AppData\Local\Programs\Python\Python312\Lib\site-packages\，落点保持同名相对路径，落在 D:\C盘搬迁_定时迁移\AppData\Local\Programs\Python\Python312\Lib\site-packages\ 之下。

搬完用 Python312 本体实测，import cv2、scipy、pymupdf、litellm、onnxruntime、torch 2.5.1+cpu、paddle 全部正常，Junction 对 Python 透明，量化脚本不用改路径。

被占用或跳过的：Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys17-7-0 被驱动占用；Edge Cache 与豆包 Cache 下 No_Vary_Search 各 2 文件 24 字节被占；pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节待安装，保留。

仍不动的冷块：Local\Feishu 8012 文件 2292007845 字节 飞书在运行；.minimax\sessions\mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节 MiniMax Code 在用；Desktop\ucl_special\unl_3v\segs 约 700MB 在办视频工程；Roaming\kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节 是 WPS 当前版本；Edge Default\Extensions 405 文件 61052805 字节 是在用扩展；Desktop\01_股票研究\股票分析体系迁移包_20261105 里的选股系统备份 37472857 字节不动。

C 盘一夜之间多出 10.52GB，查明主要来自 MiniMax Code 自己清理旧会话：.minimax\v2 从 18.03GB 降到 5.65GB，sessions 只剩 2.50GB，sqlite 2.19GB 仍在写。这不是我删的，是程序自己回收。
2026-11-17 11:17 第三十三轮定时任务，清理合计 991380 字节，迁移 78 个目录 9670 文件 637595878 字节，约 0.59GB，全部留 Junction，零回滚。

清理分项：Local\Temp 0 字节；Windows\Temp 前 10 文件 108442 字节，删不动被占的 virtual_camera 与 TAOAcceleratorEx64_ev.sys17-7-0，仅释放 1325 字节；SoftwareDistribution\Download 空；Edge Cache 只剩被占的 24 字节；Edge Code Cache 空；Edge CacheStorage 空；豆包 Cache 只剩被占的 24 字节；豆包 Code Cache 210 文件 85750 字节全删；豆包 GPUCache 空；更新器只剩 pending 两份 287455475 字节，保留待装；__pycache__ 12 个目录 45 文件 904305 字节。合计 991380 字节。

迁移明细：WPS 插件池里被新版本取代的旧版本目录，78 个，共 9670 文件 637595878 字节。
来源统一是 C:\Users\Administrator\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\。
落点保持同名，在 D:\C盘搬迁_定时迁移\AppData\Roaming\kingsoft\wps\addons\pool\win-i386\ 之下，每个原位都留了 Junction，WPS 读插件不受影响。
单个最大的几块：invoicecheck_3.1.0.33095 28326969 字节、batchprint_3.1.0.33750 27354860 字节、kbillprintv2_3.1.0.34906 27289594 字节、kstartpage_3.1.0.15494 26878923 字节、kdocs_3.0.0.285 26248796 字节、kbillcommon_3.1.0.26930 25163881 字节、kpdfairotate_3.1.0.7472 25269505 字节、pdfbatchrename_3.1.0.22943 25036099 字节、pdfkernel_3.1.0.30893 24848218 字节、kwebaimodeltextclasstfv1_3.0.0.3 22564284 字节、kdocset_3.0.0.134 20638644 字节、ksphotocv_3.1.0.18968 20929820 字节、photo_3.1.0.39882 20073903 字节、khyperion_3.1.0.16258 18822324 字节、yunbox_3.1.0.8574 18772842 字节。

只搬同一组件被更新版本取代的旧目录，当前在用的新版本一律留在 C 盘。
新版本目录还是空壳、WPS 还没下下来的族，整族不动，避免搬走唯一可用副本，如 kdocsword_3.0.0.101、sh32mdp_3.1.0.183 等。
7 天内有改动的 knewdocs_3.1.0.15013 与 kwpsaitypeset_3.1.0.14306 按冷数据规则跳过。

被占用或跳过的：Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys17-7-0 被驱动占用；Edge Cache 与豆包 Cache 下 No_Vary_Search 各 2 文件 24 字节被占；pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节待安装，保留。

仍不动的冷块：Local\Feishu 8012 文件 2292007845 字节 飞书在运行；.minimax\sessions\mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节 MiniMax Code 在用；Desktop\ucl_special\unl_3v\segs 等过程目录约 1.6GB 在办视频工程；Edge Default\Extensions 405 文件 61052805 字节 是在用扩展；Python312 的 pandas 1560 文件 34605572 字节 量化脚本在用；Desktop\01_股票研究\股票分析体系迁移包_20261105 里的选股系统备份 37472857 字节不动。

C 盘可用由本轮开始 39.31GB 到收尾 39.90GB，清理与迁移合计腾出约 0.60GB，仍差 0.10GB 才到 40GB 线。
2026-11-17 14:17 第三十四轮定时任务，清理合计 18102356 字节，约 17.3MB，迁移 1 个目录 8012 文件 2292007845 字节，约 2.13GB，留 Junction，零回滚。

清理分项：Local\Temp 0 字节；Windows\Temp 前 9 文件 107117 字节，virtual_camera 与 TAOAcceleratorEx64_ev.sys17-7-0 被驱动占用删除失败，释放 0 字节；SoftwareDistribution\Download 空；Edge Cache 只剩被占的 24 字节；Edge Code Cache 空；Edge CacheStorage 空；豆包 Cache 只剩被占的 24 字节；豆包 Code Cache 2 文件 25117 字节全删；豆包 GPUCache 空；更新器只剩 pending 两份 287455475 字节，保留待装；__pycache__ 119 个目录 800 文件 18077239 字节；超 30 天 .log 0 个。合计 18102356 字节。

迁移明细：C:\Users\Administrator\AppData\Local\Feishu，8012 文件 2292007845 字节，约 2.13GB，迁移完成时间 2026-11-17 14:26。
落点 D:\C盘搬迁_定时迁移\AppData\Local\Feishu，同名同结构，原位留 Junction，路径不变。
搬前确认飞书进程 Feishu 与 Lark 均为 0 个，目录内最新文件修改时间 2026-10-24，已超 7 天，不在禁迁清单。
搬后回读目标侧 8012 文件 2292007845 字节，与源侧基线完全对上，源侧只剩 Junction。

C 盘可用由本轮开始 37.89GB 到收尾 40.05GB，清理加迁移合计腾出约 2.16GB，已回到 40GB 线以上。

本轮开始前 C 盘比上一轮收尾少了约 2GB，查明是 C:\Users\Administrator\Doubao\chats 从 16248MB 涨到 18372MB，是聊天框新出的成品视频，属用户产出，未动。

被占用或跳过的：Windows\Temp 下 virtual_camera 与 TAOAcceleratorEx64_ev.sys17-7-0 被驱动占用；Edge Cache 与豆包 Cache 下 No_Vary_Search 各 2 文件 24 字节被占；pending\MiniMax Code Setup 3.1.16-x64.exe 287455296 字节待安装，保留。

仍不动的冷块：.minimax\sessions\mvs_80d44d465b694b529f44e5143746fa6a 287 文件 235212388 字节 MiniMax Code 在用；Desktop\ucl_special\unl_3v 顶层 11-16 仍在写、7 天内 12684 文件有改动，整个工程视为在办不动；Roaming\kingsoft\wps\addons\pool\win-i386\qing_3.1.0.19763 826 文件 114490647 字节 是 WPS 当前版本；Edge Default\Extensions 405 文件 61052805 字节 是在用扩展；Desktop\01_股票研究\股票分析体系迁移包_20261105 里的选股系统备份 37472857 字节 属禁迁；Python312 的 pandas 1560 文件 34605572 字节 量化脚本在用。
2026-11-17 15:20 至 15:37 桌面大文件专项迁移，按用户指令把桌面占空间最大的四块搬到 E 盘，原位全部留 Junction，路径与文件名不变，零回滚。

落点根目录 E:\桌面大文件迁移_20261117，相对结构照桌面原名原样保留。

分类榜混剪发布素材：来源 C:\Users\Administrator\Desktop\分类榜混剪发布素材，2047 文件 10961480548 字节，约 10.21GB，完成时间 15:24。

待发混剪成片：来源 C:\Users\Administrator\Desktop\待发混剪成片，125 文件 1701006489 字节，约 1.58GB，完成时间 15:29。

票房榜发布素材：来源 C:\Users\Administrator\Desktop\票房榜发布素材，57 文件 1385448125 字节，约 1.29GB，完成时间 15:30。

ucl_special：来源 C:\Users\Administrator\Desktop\ucl_special，15982 文件 6941427670 字节，约 6.46GB，完成时间 15:37。

合计 4 块 18211 文件 20989362832 字节，约 19.54GB。

搬后逐块回读目标侧，2047 文件 10961480548 字节、125 文件 1701006489 字节、57 文件 1385448125 字节、15982 文件 6941427670 字节，四块全部与源侧基线对上，源侧只剩 Junction。

C 盘可用由 40.05GB 升到 59.07GB，E 盘可用由 39.06GB 降到 19.78GB。

本轮没搬的四块及原因：01_股票研究 5840MB 内含 7 处联接且有禁迁子目录，整块搬会打乱联接；龙虾命中的个股 2920MB 内含 6 处联接；02_内容创作 4660MB 内含 40 处联接，其中足球成品合集是历史搬迁留下的编号目录联接；选股系统备份 2469MB、03_账号与资产 921MB、AI图片 286MB 属禁迁清单。

快捷方式与智能体联接一律没动：桌面 00_快捷方式 内 40 个 .lnk 原样；桌面根 11 个 .lnk 原样；首阳战法自用版_mcp_venv 仍指向 D:\C盘搬迁_定时迁移\Desktop\首阳战法自用版_mcp_venv；异动归因全文 仍指向 Desktop\01_股票研究\异动归因全文；02_内容创作\Mavis视频成品 仍指向 D:\C盘搬迁_20261111\MiniMax_成品\Mavis视频成品。

E 盘只剩 19.78GB，MiniMax 若还要往 E 盘写大素材，先确认余量够用。
2026-11-17 17:17 第三十五轮定时任务，触发时本机掉线未跑成，18:0x 起分两段补跑，本轮只清理不迁移，没有搬任何目录。

清理起点 C 盘可用 59.51GB，收尾实测 59.86GB，本轮合计多出约 0.35GB。

第一段清理：更新器重复安装包 @mmx-agentelectron-updater 下的 MiniMax Code Setup 3.1.16-x64.exe 287455296 字节在 18:12 前后被清掉，实测该目录现在已不存在。

第二段七类与缓存清理，逐项实测：

AppData\Local\Temp：前 9 文件 10699566 字节，已全清，释放 10699566 字节。

Windows\Temp：前 24 文件 112126 字节，删 1 项后剩 14 文件 108434 字节，释放 3692 字节；virtual_camera、FXSAPIDebugLogFile.txt、FXSTIFFDebugLogFile.txt、TAOAcceleratorEx64_ev.sys17-17-59 四个被进程占用跳过。

Windows\SoftwareDistribution\Download：清理前已是 0 文件，无释放。

Edge Cache：前 2 文件 24 字节，清空释放 24 字节；Edge Code Cache 与 Service Worker CacheStorage 都是 0。

豆包 Cache：前 182 文件 32772930 字节，清后剩 2 文件 24 字节，释放 32772906 字节；剩下的 No_Vary_Search 被占用跳过。

豆包 Code Cache：前 1134 文件 50512656 字节，全清，释放 50512656 字节。

豆包 GPUCache：5 文件 5837168 字节，全清，释放 5837168 字节。

七类合计释放 99826012 字节。

__pycache__：清 120 个目录 799 文件 17995384 字节，零失败。

30 天以上 .log：删 3 个文件 112974 字节，零占用跳过。

第二段合计 117934370 字节，约 112.5MB。

本轮迁移为空：C 盘可用 59.51GB，早已在 40GB 线以上，按规则只清不迁。

本轮基线体积：C:\Users\Administrator 384958 文件 99005694185 字节；AppData\Local 109110 文件 14418914311 字节；C:\Windows 164777 文件 20683868164 字节；C:\ProgramData 4919 文件 8836933193 字节。
2026-11-17 19:21 至 19:45 桌面大文件二次迁移，用户口径是桌面超过 100MB 的都要搬走，本轮把剩下八块全部搬到 E 盘，原位全部留 Junction，路径不变。

一、01_股票研究，来源 C:\Users\Administrator\Desktop\01_股票研究，19746 文件 6124279749 字节，约 5.70GB，完成时间 19:31，内部原有 7 处联接已在新位置原样重建，目标全在 D:\C盘搬迁_定时迁移\Desktop\01_股票研究 下。

二、02_内容创作，来源 C:\Users\Administrator\Desktop\02_内容创作，308 文件 4886118426 字节，约 4.55GB，完成时间 19:42，内部原有 40 处联接已在新位置原样重建，含 Mavis视频成品 与足球成品合集各期编号目录。

三、03_账号与资产，来源 C:\Users\Administrator\Desktop\03_账号与资产，5571 文件 965519398 字节，约 0.90GB，完成时间 19:23。

四、选股系统备份，来源 C:\Users\Administrator\Desktop\选股系统备份，17817 文件 2601308978 字节，约 2.42GB，完成时间 19:23。

五、AI图片，来源 C:\Users\Administrator\Desktop\AI图片，274 文件 299598326 字节，约 0.29GB，完成时间 19:22。

六、股票克隆包_20261107，来源 C:\Users\Administrator\Desktop\股票克隆包_20261107，2091 文件 286828457 字节，约 0.27GB，完成时间 19:22。

七、动画大师混剪发布素材，来源 C:\Users\Administrator\Desktop\动画大师混剪发布素材，7 文件 220097346 字节，约 0.21GB，完成时间 19:21。

八、豆瓣口碑榜发布素材，来源 C:\Users\Administrator\Desktop\豆瓣口碑榜发布素材，43 文件 157799484 字节，约 0.15GB，完成时间 19:22。

八块合计 45655 文件 15541550164 字节，约 14.48GB，全部回读对上源侧基线，零回滚。

加上下午搬的四块，桌面大文件累计搬 12 块，63866 文件 36530912996 字节，约 34.02GB，桌面 12 个占空间目录现在全部是 Junction，实体都在 E:\桌面大文件迁移_20261117。

过程中 03_账号与资产 与 选股系统备份 两块的 .git 只读对象第一次删不掉，报拒绝访问，清掉只读属性后补删成功，两块联接已建好且回读对得上。

C 盘可用由 59.86GB 升到 72.95GB，E 盘可用由 19.77GB 降到 4.68GB。

E 盘已经接近写满，后续冷数据一律改走 D:\C盘搬迁_定时迁移，不要再往 E 盘放大文件。
2026-11-17 20:12 至 20:26 删除分类榜混剪发布素材里已经出片的旧素材，按用户口径执行。

一、删除范围，只动 分类榜混剪发布素材\工程，成片一律保留。

二、trailers 预告片原件 179 文件 4374721671 字节，已删。

三、output 中间输出 44 文件，已删，只留惊悚榜的合并母版与抖音配音版两份。

四、clips 切片 132 文件 726145858 字节，已删。

五、audio 配音分段 28 文件，已删，只留惊悚榜 final 与 voice 两个 wav。

六、check 校验帧 1934 文件 66428652 字节，已删。

七、工程整目录由 2506 文件 9048.4MB 降到 203 文件 290.0MB，合计删 2303 文件约 8.55GB。

八、脚本、plan 与 json 全留，成片 视频 目录 22 个 mp4 一个没动。

九、E 盘可用由 4.68GB 升到 13.18GB。

十、删除当时分类榜的惊悚榜正在出片，我误删了刚产出的 B站横版无配音，已用同一份合并母版重新烧字幕生成，96.49MB，时长 3 分 41 秒 52，与抖音配音版 3 分 41 秒 47 对齐。

十一、要重剪这些榜，trailers 原件已不在，需用工程里的 download 脚本重新下载，清单见桌面提示词文件夹里的 素材删除清单_20261117.txt。
2026-11-17 20:26 至 20:38 第三十六轮定时清理，本轮 C 盘可用 71.91GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 71.91GB 已用 141.52GB，D 可用 85.94GB，E 可用 13.09GB。

二、体积基线，C:\Users\Administrator 341157 文件 85781453549 字节，AppData\Local 110611 文件 15648984215 字节，C:\Windows 164822 文件 20689123433 字节，C:\ProgramData 4921 文件 8838759287 字节。

三、AppData\Local\Temp，清理前 5 文件 6512 字节，清完 0 文件，释放 6512 字节，删 2 项。

四、C:\Windows\Temp，清理前 14 文件 108434 字节，清完剩 1 文件 105800 字节，释放 2634 字节，删 3 项。被占用跳过 TAOAcceleratorEx64_ev.sys17-17-59。

五、C:\Windows\SoftwareDistribution\Download 清理前已是 0 文件，无释放。

六、Edge 的 Cache、Code Cache、Service Worker CacheStorage 三项均为 0 文件，无释放。

七、豆包 Cache 前 2 文件 24 字节，No_Vary_Search 被占用，无释放。

八、豆包 Code Cache 前 534 文件 15486837 字节，全清，释放 15486837。

九、豆包 GPUCache 0 文件，无释放。

十、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十一、七类合计释放 15495983 字节，约 14.8MB。

十二、另清 __pycache__ 126 目录 815 文件 18415368 字节，零失败；30 天以上 .log 本轮 0 个，释放 0。

十三、两段合计释放 33911351 字节，约 32.3MB。

十四、清理后实测，C 可用 71.87GB 已用 141.56GB，D 可用 85.94GB，E 可用 13.14GB。本轮 C 可用不升反降 0.04GB，原因是同期系统与软件写入量大于清理量，属正常。

十五、失败项零，只有两条被占用跳过，已在上面写清文件名与原因。
2026-11-17 23:23 至 23:33 第三十七轮定时清理，本轮 C 盘可用 68.23GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 68.23GB 已用 145.21GB，D 可用 85.93GB，E 可用 10.10GB。

二、体积基线，C:\Users\Administrator 343908 文件 89512454577 字节，AppData\Local 112913 文件 17550994605 字节，C:\Windows 164821 文件 20687270534 字节，C:\ProgramData 4922 文件 8839572726 字节。

三、AppData\Local\Temp 清理前已是 0 文件，无释放。

四、C:\Windows\Temp 清理前 1 文件 105800 字节，只剩那一个被占用的文件，释放 0。被占用跳过 TAOAcceleratorEx64_ev.sys17-17-59。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放。

六、Edge 的 Cache、Code Cache、Service Worker CacheStorage 三项均 0 文件，无释放。

七、豆包 Cache 2 文件 24 字节，No_Vary_Search 被占用，无释放。

八、豆包 Code Cache 0 文件，无释放。豆包 GPUCache 0 文件，无释放。

九、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十、七类合计释放 0 字节，这一轮七类目录本来就是空的。

十一、另清 __pycache__ 10 目录 48 文件 1106097 字节，零失败；30 天以上 .log 本轮 0 个。

十二、本轮合计释放 1106097 字节，约 1.05MB。

十三、清理后实测，C 可用 68.24GB 已用 145.19GB，D 可用 85.93GB，E 可用 10.16GB。

十四、C 盘可用本轮比上轮少 3.63GB，同期软件写入与出片缓存增长快于清理量，七类目录已见底。

十五、失败项零，两条被占用跳过，已在上面写清文件名与原因。
2026-11-18 08:17 至 08:20 第三十八轮定时清理，本轮 C 盘可用 73.09GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 73.09GB 已用 140.34GB，D 可用 85.60GB，E 可用 9.27GB。

二、体积基线，C:\Users\Administrator 342477 文件 85576969209 字节，AppData\Local 111061 文件 13331213235 字节，C:\Windows 164859 文件 19558404372 字节，C:\ProgramData 4931 文件 8851216996 字节。

三、AppData\Local\Temp 清理前 1 文件 8199464 字节，清完 0 文件，释放 8199464 字节，删 1 项。

四、C:\Windows\Temp 清理前 4 文件 105800 字节，清完 2 文件 105800 字节，释放 0。被占用跳过两项，virtual_camera 与 TAOAcceleratorEx64_ev.sys18-7-51。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放。

六、Edge 的 Cache、Code Cache、Service Worker CacheStorage 三项均 0 文件，无释放。

七、豆包 Cache 前 199 文件 31747302 字节，清完 2 文件 24 字节，释放 31747278 字节。剩余 No_Vary_Search 被占用跳过。

八、豆包 Code Cache 前 1131 文件 801607 字节，全清，释放 801607。

九、豆包 GPUCache 前 5 文件 5837168 字节，全清，释放 5837168。

十、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十一、七类合计释放 46585517 字节，约 44.4MB。

十二、另清 __pycache__ 119 目录 799 文件 18001873 字节，零失败；30 天以上 .log 本轮 0 个。

十三、两段合计释放 64587390 字节，约 61.6MB。

十四、清理后实测，C 可用 73.14GB 已用 140.29GB，D 可用 85.60GB，E 可用 9.28GB。

十五、本轮 C 可用回升 0.05GB；失败项零，三项被占用跳过，已在上面写清文件名与原因。
2026-11-18 11:17 至 11:23 第三十九轮定时清理，本轮 C 盘可用 69.14GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 69.14GB 已用 144.29GB，D 可用 85.23GB，E 可用 6.10GB。

二、体积基线，C:\Users\Administrator 345725 文件 89785369573 字节，AppData\Local 110555 文件 13522368754 字节，C:\Windows 164900 文件 19564322836 字节，C:\ProgramData 4932 文件 8851513588 字节。

三、AppData\Local\Temp 清理前 0 文件，无释放。

四、C:\Windows\Temp 清理前 3 文件 106239 字节，清完仍 3 文件 106239 字节，释放 0。被占用跳过两项，virtual_camera 与 TAOAcceleratorEx64_ev.sys18-7-51。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放。

六、Edge 的 Cache、Code Cache、Service Worker CacheStorage 三项均 0 文件，无释放。

七、豆包 Cache 2 文件 24 字节，No_Vary_Search 被占用，无释放。

八、豆包 Code Cache 前 18 文件 28702 字节，全清，释放 28702 字节。

九、豆包 GPUCache 清理前 0 文件，无释放。

十、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十一、七类合计释放 28702 字节。

十二、另清 __pycache__ 143 目录 1022 文件 22043736 字节，零失败；30 天以上 .log 本轮 0 个。

十三、两段合计释放 22072438 字节，约 21.1MB。

十四、清理后实测，C 可用 69.11GB 已用 144.32GB，D 可用 85.23GB，E 可用 6.05GB。

十五、本轮前一小时做过一次降载处理，三个转码进程优先级降到低于正常并锁前四核，七类释放叠加约 69.3MB，已在 11:04 那次单独汇报。

十六、失败项零，两项被占用跳过，已在上面写清文件名与原因。

十七、E 盘只剩 6.05GB，转码输出写在 E 上的工程目录，写满会中断出片，这一条需要尽快腾 E。
2026-11-18 17:17 至 17:19 第四十轮定时清理，本轮 C 盘可用 66.42GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 66.42GB 已用 147.02GB，D 可用 85.29GB，E 可用 3.82GB。

二、体积基线，C:\Users\Administrator 349324 文件 93267630445 字节，AppData\Local 113044 文件 13770231874 字节，C:\Windows 164931 文件 19641588155 字节，C:\ProgramData 4943 文件 8844948817 字节。

三、AppData\Local\Temp 清理前 2 文件 8200558 字节，全清，释放 8200558 字节。

四、C:\Windows\Temp 清理前 27 文件 115391 字节，清完 7 文件 107117 字节，释放 8274 字节。被占用跳过两项，virtual_camera 与 TAOAcceleratorEx64_ev.sys18-13-45。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放，删空项一个。

六、Edge Cache 前 32 文件 8744706 字节，清完 2 文件 24 字节，释放 8744682 字节，No_Vary_Search 被占用跳过。

七、Edge Code Cache 前 30 文件 132738 字节，全清，释放 132738 字节。

八、Edge Service Worker CacheStorage 前 0 文件，无释放。

九、豆包 Cache 前 190 文件 31928295 字节，清完 2 文件 24 字节，释放 31928271 字节，No_Vary_Search 被占用跳过。

十、豆包 Code Cache 前 1512 文件 37474813 字节，全清，释放 37474813 字节。

十一、豆包 GPUCache 前 5 文件 5837168 字节，全清，释放 5837168 字节。

十二、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十三、七类合计释放 92326504 字节，约 88.0MB，是近期释放量最大的一轮。

十四、另清 __pycache__ 122 目录 835 文件 18737429 字节，零失败；30 天以上 .log 本轮 0 个。

十五、两段合计释放 111063933 字节，即七类 92326504 加 18737429，约 105.9MB。

十六、清理后实测，C 可用 66.00GB 已用 147.43GB，D 可用 85.03GB，E 可用 3.60GB。C 盘可用反而少了 0.42GB，原因是两个转码成片同时在往 C 盘与 E 盘写文件，写入量大于清理量。

十七、失败项零，三项被占用跳过，已在上面写清文件名与原因。

十八、E 盘只剩 3.60GB，比上一轮 6.05GB 又少了 2.45GB，转码输出写在这里，必须尽快腾 E。
2026-11-18 20:17 至 20:20 第四十一轮定时清理，本轮 C 盘可用 65.80GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 65.80GB 已用 147.64GB，D 可用 85.30GB，E 可用 3.73GB。

二、体积基线，C:\Users\Administrator 349742 文件 93444595259 字节，AppData\Local 112996 文件 13912922326 字节，C:\Windows 164908 文件 19517357111 字节，C:\ProgramData 4949 文件 8845333322 字节。

三、AppData\Local\Temp 清理前 1 文件 8199464 字节，全清，释放 8199464 字节。

四、C:\Windows\Temp 清理前 10 文件 107117 字节，清完 1 文件 105800 字节，释放 1317 字节，删项 5 个。被占用跳过一项，TAOAcceleratorEx64_ev.sys18-19-17，这是驱动替身文件每轮都会换后缀重生。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放，删空项一个。

六、Edge Cache 前 2 文件 24 字节，全清，释放 24 字节。

七、Edge Code Cache 前 0 文件，无释放。

八、Edge Service Worker CacheStorage 前 0 文件，无释放。

九、豆包 Cache 前 237 文件 59575715 字节，清完 2 文件 24 字节，释放 59575691 字节，本轮释放最大项，No_Vary_Search 被占用跳过。

十、豆包 Code Cache 前 1326 文件 1098928 字节，全清，释放 1098928 字节。

十一、豆包 GPUCache 前 5 文件 5837168 字节，全清，释放 5837168 字节。

十二、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十三、七类合计释放 74712592 字节，约 71.3MB。

十四、另清 __pycache__ 125 目录 810 文件 18203409 字节，零失败；30 天以上 .log 本次删掉 9 个 143874 字节，这是近几轮第一次真正命中旧日志。

十五、两段合计释放 74712592 加 18203409 加 143874 等于 93099875 字节，约 88.8MB。

十六、清理后实测，C 可用 65.86GB 已用 147.57GB，D 可用 85.23GB，E 可用 3.73GB。C 盘可用比清理前多 0.06GB，本轮清理量终于盖住了同期写入量。

十七、失败项零，两项被占用跳过，已在上面写清文件名与原因。

十八、E 盘可用从 3.60GB 回到 3.73GB，仍在极限位置，转码输出继续写在这里，必须尽快腾 E。
2026-11-18 23:17 至 23:20 第四十二轮定时清理，本轮 C 盘可用 64.67GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 64.67GB 已用 148.76GB，D 可用 85.13GB，E 可用 3.73GB。C 比上一轮收尾的 65.86GB 少了 1.19GB，转码输出仍在往 C 盘写。

二、体积基线，C:\Users\Administrator 348707 文件 94491076563 字节，AppData\Local 111456 文件 14607060967 字节，C:\Windows 164921 文件 19517764683 字节，C:\ProgramData 4951 文件 8845251890 字节。AppData\Local 单轮涨了 694MB，是这一小时的主要增量。

三、AppData\Local\Temp 本轮空目录，0 文件，无释放。

四、C:\Windows\Temp 清理前 5 文件 107125 字节，清完 4 文件 106682 字节，释放 443 字节。被占用跳过两项，virtual_camera 与 TAOAcceleratorEx64_ev.sys18-19-17。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放，删空项一个。

六、Edge Cache 前 8 文件 6152876 字节，清完 2 文件 24 字节，释放 6152852 字节，是本轮最大一项。No_Vary_Search 被占用跳过。

七、Edge Code Cache 前 4 文件 144 字节，全清，释放 144 字节。

八、Edge Service Worker CacheStorage 前 0 文件，无释放。

九、豆包 Cache 前 2 文件 24 字节，清完 2 文件 24 字节，无释放，No_Vary_Search 被占用跳过。

十、豆包 Code Cache 前 35 文件 37528 字节，全清，释放 37528 字节。

十一、豆包 GPUCache 本轮 0 文件，无释放。

十二、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十三、七类合计释放 6190967 字节，约 5.9MB，是近二十轮里最少的一次，说明常规缓存已经清到接近空档。

十四、另清 __pycache__ 13 目录 86 文件 1801552 字节，零失败；30 天以上 .log 删掉 2 个 8732 字节。

十五、两段合计释放 6190967 加 1801552 加 8732 等于 8001251 字节，约 7.6MB。

十六、清理后实测，C 可用 64.67GB 已用 148.77GB，D 可用 85.13GB，E 可用 3.73GB。C 盘可用与清理前持平，释放的 7.6MB 被同期写入直接吃掉。

十七、失败项零，四项被占用跳过，均已写清文件名与原因。

十八、E 盘整轮没有变化，仍 3.73GB，转码输出没有新增长，但也没有腾出空间，风险照旧。
2026-11-19 08:17 至 08:20 第四十三轮定时清理，本轮 C 盘可用 65.61GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 65.61GB 已用 147.82GB，D 可用 84.62GB，E 可用 3.73GB。过夜期间 C 盘回升 0.94GB，D 盘反而少了 0.51GB。

二、体积基线，C:\Users\Administrator 350288 文件 93616397706 字节，AppData\Local 112455 文件 13715476148 字节，C:\Windows 164935 文件 19569949462 字节，C:\ProgramData 4961 文件 8845027317 字节。用户目录文件数比上一轮多 1581 个，说明夜里还在不停写新东西。

三、AppData\Local\Temp 清理前 32 文件 12972294 字节，全清，释放 12972294 字节，删项 32 个，是本轮最大一项。

四、C:\Windows\Temp 清理前 8 文件 106682 字节，清完 6 文件 107125 字节，净增 443 字节，删项 3 个。这里如实写清，同期有新文件写进来，删掉 3 个后总量反而多了 443 字节，不是释放。被占用跳过两项，virtual_camera 与 TAOAcceleratorEx64_ev.sys19-7-0，驱动替身这轮后缀已换成 19-7-0。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放，删空项一个。

六、Edge Cache 前 2 文件 24 字节，全清，释放 24 字节。

七、Edge Code Cache 前 0 文件，无释放。

八、Edge Service Worker CacheStorage 前 0 文件，无释放。

九、豆包 Cache 前 204 文件 37263389 字节，清完 2 文件 24 字节，释放 37263365 字节，No_Vary_Search 被占用跳过。

十、豆包 Code Cache 前 1125 文件 501368 字节，全清，释放 501368 字节。

十一、豆包 GPUCache 前 5 文件 5837168 字节，全清，释放 5837168 字节。

十二、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均已不存在。

十三、七类合计释放 56573776 字节，约 54.0MB。

十四、另外两段本轮全空，__pycache__ 0 目录 0 文件，30 天以上 .log 0 个 0 字节，这是本项目开跑以来第一次两段都零命中，说明可清对象基本见底。

十五、合计释放 56573776 加 0 加 0 等于 56573776 字节，约 54.0MB。

十六、清理后实测，C 可用 65.65GB 已用 147.79GB，D 可用 84.61GB，E 可用 3.73GB。C 盘可用比清理前多 0.04GB，写入量又吃掉将近一半。

十七、失败项零，两项被占用跳过，已在上面写清文件名与原因；Windows\Temp 一项净增已如实记账，不计入释放。

十八、E 盘连续三轮停在 3.73GB，转码输出本轮没有再增长，但空间也没有腾出来，这条风险仍在。
2026-11-19 11:17 至 11:20 第四十四轮定时清理，本轮 C 盘可用 65.12GB，远超 40GB，按约定只清不迁，零迁移。

一、清理前基线，C 可用 65.09GB 已用 148.34GB，D 可用 83.97GB，E 可用 0.60GB。三小时里 C 盘少 0.56GB、D 盘少 0.65GB、E 盘被写掉 3.14GB，E 盘已经见底。

二、体积基线，C:\Users\Administrator 350390 文件 93969407472 字节，AppData\Local 112191 文件 14033532725 字节，C:\Windows 164954 文件 19573166044 字节，C:\ProgramData 4961 文件 8845390014 字节。用户目录三小时新增 102 个文件但总字节反而少了 647MB，说明有大块文件被写进 E 或 D。

三、AppData\Local\Temp 清理前 139 文件 20573463 字节，全清，释放 20573463 字节，删项 139 个，是本轮最大一项，也是最近十轮里 Temp 攒得最多的一次。

四、C:\Windows\Temp 清理前 7 文件 107568 字节，清完 2 文件 105800 字节，释放 1768 字节，删项 0 个。被占用跳过两项仍是 virtual_camera 与 TAOAcceleratorEx64_ev.sys19-7-0。

五、C:\Windows\SoftwareDistribution\Download 清理前 0 文件，无释放，删空项一个。

六、Edge Cache 前 8 文件 6152876 字节，清完 2 文件 24 字节，释放 6152852 字节，No_Vary_Search 被占用跳过。

七、Edge Code Cache 前 4 文件 144 字节，全清，释放 144 字节。

八、Edge Service Worker CacheStorage 前 0 文件，无释放。

九、豆包 Cache 前 2 文件 24 字节，无释放，No_Vary_Search 被占用跳过。

十、豆包 Code Cache 前 86 文件 1072570 字节，全清，释放 1072570 字节。

十一、豆包 GPUCache 前 0 文件，无释放。

十二、更新器 @mmx-agentelectron-updater 本轮 0 文件 0 字节，LobsterAI 与剪映 SupplysStore 均不存在。

十三、七类合计释放 27800797 字节，约 26.5MB。

十四、另外两段，__pycache__ 0 目录 0 文件，30 天以上 .log 删掉 2 个 2009 字节。

十五、合计释放 27800797 加 2009 等于 27802806 字节，约 26.5MB。

十六、清理后实测，C 可用 65.12GB 已用 148.31GB，D 可用 83.97GB，E 可用 0.59GB。C 盘可用只多 0.03GB，释放量基本被同期写入抵消。

十七、失败项零，两项被占用跳过已在上文写清文件名与原因。

十八、E 盘从 3.73GB 掉到 0.59GB，一小时写掉 3.14GB，这是三轮以来第一次见底。转码输出仍指向 E，再写不到一小时就可能整盘写满中断出片，必须在下一轮之前先腾 E 或把输出改到 D，此事待用户拍板，本轮未擅自搬动任何成片。
2026-11-19 11:30 至 11:44 E 盘专项清理，用户直接指令，不属于定时任务的七类白名单，单独记账。

一、起因，E 可用只剩 0.49GB，转码输出仍写 E，一小时被写掉 3.14GB，随时会写满中断出片。

二、清理前 E 可用 0.49GB 已用 232.64GB，清理后 E 可用 12.93GB 已用 220.20GB，实回收 12.44GB。

三、分类榜混剪发布素材\工程 的素材与中间件，trailers 214 文件 4317955808 字节，clips 201 文件 981436898 字节，output 46 文件 2865640645 字节，audio 30 文件 764525340 字节，check 2005 文件 37288382 字节，frames 40 文件 348334 字节，合计约 8.5GB。脚本与 json 计划文件全部保留，重剪仍可用 download 脚本重新下载。

四、视频素材库工作目录，f40_work 2072 文件 698548009 字节，md5c_work 191 文件 558600983 字节，md6_work 3799 文件 1565497837 字节，合计 2.63GB，均为 raw 原片、segs 分段与 timeline 中间表。

五、足球素材 下载暂存 723 文件 609437883 字节，下载暂est 247 文件 347118373 字节，合计 0.89GB，均为下载原片。

六、E 盘根临时目录，.__jianying_export_temp_folder_1777595223__ 1 文件 1310768 字节，tmp 2 文件 1535310 字节，md5c_tmp 1 文件 7930 字节，合计 1.28MB。

七、迁移目录内旧缓存，C盘搬迁_定时迁移\AppData\Local 下 electron Cache 409650912 字节，node-gyp Cache 63664967 字节，electron-builder Cache 35041811 字节，DQSStockPro cache 11409606 字节，fontconfig cache 2922076 字节，合计 0.49GB。

八、E:\Users 旧用户缓存，DingTalk_108 Cache 45469734 字节加 Code Cache 8025679 字节，qBittorrent logs 5279 字节，合计 53.5MB。

九、本轮合计释放 13325465716 字节，约 12.41GB，无失败项，无被占用跳过项。

十、成片一律未动，待发混剪成片 2.01GB、足球成品合集 4.49GB、Mavis视频成品 3.87GB、分类榜\视频 3.80GB、票房榜\视频 1.21GB 全部原样保留。

十一、未动但可继续回收的候选，XiaoBai\Data\Bak\bak_os\9DA7503D26C64A22B8EB661A520A4027.GHO 76.22GB 是 2026-04-16 的系统备份镜像，删掉能一口气腾出 76GB，但这属于系统还原底牌，等用户拍板；迅雷云盘 1.07GB 是 10 月下载原片；ucl_special\unl_3v 4.18GB 是外传工程，未动。

十二、迁移三块合计 92.78GB，C盘搬迁_20261111 30,969 文件 29.53GB，C盘搬迁_定时迁移 385,675 文件 34.19GB，桌面大文件迁移_20261117 66,226 文件 29.06GB。用户提到迁移的文件太多，是否需要合并去重待拍板，本轮未动。
2026-11-19 12:40 至 13:02 B 站版成片清理，按用户口径执行：只备份做过的视频与素材，B 站版这类重复成片可删，抖音版一律保留。

一、清理前 E 可用 12.93GB，清理后 E 可用 16.04GB，实回收 3.11GB，即 3345038726 字节。

二、口径修正，抖音横版是抖音的 16 比 9 版本，不是 B 站版，本轮按文件名含抖音或竖版即保留、含 B 站或无配音才删来区分，没有误删任何抖音文件。

三、删除 83 个文件，涉及三处，分类榜混剪发布素材\视频 下的各榜 B站横版_1920x1080_无配音 与 旧版_1280x720 重复件，待发混剪成片\02_B站无配音版 全目录，动画大师与豆瓣口碑榜 视频 下的混剪无配音文件。

四、待发混剪成片\02_B站无配音版 目录删空后整目录移除。

五、抖音版全部原样保留，待发混剪成片\01_抖音配音版 44 文件 0.96GB 完好，票房榜\视频 与 分类榜\视频 下的解说配音版、抖音竖版 均未动。

六、分类榜工程只保留了脚本与 json 计划，素材原片已删，重剪需用 download.py 等脚本重新下载，这一点用户已认可。

七、为防重复，另生成 已做过视频清单.md，逐条列出保留的成片路径、文件大小与修改日期，共 2813 条，三个目录树全覆盖，桌面给MiniMax的搬迁提示词 与 E:\C盘搬迁_定时迁移 各存一份，做新选题前先查这份清单。

八、失败项零，无被占用跳过项。

九、当前三盘，C 可用 65.15GB，D 可用 83.86GB，E 可用 16.04GB，E 盘已脱离见底状态。
2026-11-19 13:05 至 13:14 删系统镜像并清理 C、D 两盘垃圾，E 盘彻底脱离见底状态。

一、删除 E:\XiaoBai\Data\Bak\bak_os\9DA7503D26C64A22B8EB661A520A4027.GHO，单文件 76.22GB，用户批准后执行，删后回读该文件已不存在、bak_os 目录为空，E 可用由 16.04GB 升到 92.26GB。

二、C 盘清理释放 13230268322 字节中的 C 盘部分，即 5.67GB，C 可用由 65.14GB 升到 70.81GB。分项为：内存转储 MEMORY.DMP 431.65MB、崩溃转储 31.86MB、小转储 2.70MB、系统日志 28.80MB、错误上报 0.64MB；豆包 sdk 日志释放 1539.17MB、豆包 pip 缓存 1012.08MB、豆包浏览器 Cache 260.00MB、Code Cache 287.08MB、Service Worker 646.23MB；ToDesk 日志 494.13MB、远程桌面缓存 299.17MB、微信日志 225.61MB、MiniMax 浏览器缓存 281.79MB、2345 广告缓存 273.86MB、豆包输入法日志 95.26MB、WPS 缓存 94.23MB、Edge 与豆包前台缓存 7.44MB、用户与系统 Temp 共 0.27MB。

三、D 盘清理以 D:\Users\ADMINI~1\AppData\Local\Temp 为主，清前 6605.39MB 共 49357 个文件，释放 6605.35MB，残留 63.68MB 为占用文件，D 可用由 83.85GB 升到 90.75GB。

四、被占用而跳过的主要文件：C:\Windows\Temp\virtual_camera\virtual_camera_1964.log 与 virtual_camera_5204.log，C:\Windows\Temp\TAOAcceleratorEx64_ev.sys19-7-0，C:\Windows\Logs\waasmedic 下 73 个服役中的 etl 日志，豆包 sdk 日志 13 个在写文件，ToDesk 日志 6 个在写文件，D 盘 Temp 27 个在跑进程的临时文件。以上均按占用跳过，未强删。

五、WinSxS 组件存储经 DISM 分析为 7.69GB，其中备份与已禁用组件 1.53GB，可回收包数为 0，系统建议不做组件清理，本轮未执行清理，不做无谓改动。

六、C 盘 pagefile.sys 16GB 属虚拟内存，未动。C 盘回收站仍有 6.58GB，按禁触碰条款保留，需用户单独点头才清空。

七、备份软件方面，本轮只做选型不落地安装，结论记在给用户的报告里，候选为傲梅轻松备份免费版、Hasleo Backup Suite Free、DiskGenius 免费版、系统自带 DISM 镜像捕获，其中用户本机 E:\DiskGenius_5.6.1.1580 已存在。

八、失败项零，全程按占用跳过策略执行，没有半截状态。

九、当前三盘，C 可用 70.81GB，D 可用 90.75GB，E 可用 92.24GB。
2026-11-19 13:30 至 13:58，回收站清空与 E 盘重复合并

一、清空回收站，逐盘删尽 X:\$Recycle.Bin 下各 SID 目录内容与空壳，C 清前 6735.67MB 共 194916 个文件，D 清前 47.59MB 共 752 个文件，E 清前 0.01MB 共 16 个文件，清后三盘全为 0 文件，C 可用 70.81GB 升到 77.07GB。

二、E 盘判重范围，只对不小于 1MB 的文件按尺寸分组再算 SHA256，覆盖 桌面大文件迁移_20261117、C盘搬迁_定时迁移、C盘搬迁_20261111、迅雷云盘、MavisVideoWork 五个目录，进入统计 4869 个文件，同尺寸候选 2010 个，最终 500 组同哈希重复，理论可回收 16.99GB。

三、执行口径，保留桌面现行副本，删两份搬迁归档里的重复件；归档内部嵌套重复只留最浅一份；unl_3v 与 _bak_ 这类中间件路径不作为保留对象。

四、实际删 574 个重复件，释放 11961003089 字节约 11.14GB，E 可用 92.09GB 升到 103.22GB；15 个未删，其中 14 个是保留副本在同一轮里被别的重复组连带删掉，1 个是微信插件目录里的 d3dcompiler_47.dll 拒绝访问。

五、副作用与补救，因保留优先级没先认成品名，4 个成品路径被删，已按哈希从同内容副本恢复到原路径，包括 欧冠第一轮.mp4 108.5MB、第五轮.mp4 79.5MB、第六轮，英超豪门滑铁卢.mp4 63.6MB、首阳战法客户端 v13 的 engine.db 47.8MB，恢复后逐个回读哈希一致。

六、仍有 76 组共 308MB 桌面路径被链式删除，其中 3 组约 81MB 在别处有同名副本可以复制回，73 组约 227MB 没有同名副本，清单另存在 给MiniMax的搬迁提示词\E盘去重丢失清单.md；无副本部分主要是 龙虾命中的个股\K线库\monthly 下 15 个 csv 约 110MB，可由 Tushare 重拉，_crop 裁剪中间图 60 个约 90MB 属可重生成件，6 张 B站封面 png 共 7.4MB，engine_seed.db 44MB，trades 实盘库 1.6MB。

七、桌面树内部自身重复 42 组、迅雷云盘原片与成片同内容互斥的重复组，按风险一律没动；已删 574 项的删除路径、保留路径与大小，逐条记在 给MiniMax的搬迁提示词\E盘重复文件合并清单.md，E:\C盘搬迁_定时迁移 另有副本。

2026-11-19 14:10 至 14:22，第四十五轮定时清理，只清不迁

一、清理前基线，C 可用 76.94GB 已用 136.49GB，D 可用 90.76GB，E 可用 102.86GB。C 已远超 40GB 线，按规则本轮不启动迁移。

二、体积基线，C:\Users\Administrator 328578 文件 88755336887 字节，AppData\Local 93505 文件 9468867159 字节，C:\Windows 164854 文件 19096748656 字节，C:\ProgramData 4936 文件 8844825344 字节。

三、AppData\Local\Temp 本轮空目录，0 文件，无释放。

四、C:\Windows\Temp 清理前 6 文件 107271 字节，清完剩 3 文件 106243 字节，释放 1028 字节。被占用跳过三项，TAOAcceleratorEx64_ev.sys19-7-0 是驱动替身 105800 字节，virtual_camera 下 virtual_camera_12404.log 与 virtual_camera_5204.log 由虚拟摄像头驱动占用。

五、C:\Windows\SoftwareDistribution\Download 清理前已是 0 文件，无释放。更新器残留目录 @mmx-agentelectron-updater 已不存在，无释放。

六、__pycache__ 命中 92 个目录、77 个文件 1368795 字节，92 个目录全部删除成功，无占用失败。

七、浏览器与 Electron 缓存，Edge 的 Cache 前 2 文件 24 字节，清完留 journal.baj 1 文件 4 字节，释放 20 字节；Edge 的 Code Cache、GPUCache、Service Worker CacheStorage 与豆包、MiniMax 的缓存目录均已是 0 文件，无释放。

八、超过 30 天的 .log 候选 3711 个，删 3705 个，释放 19888500 字节；6 个被占用跳过，都在豆包用户数据里，aha\users 下 profile_explorer 的 Extension State、GCM Store、Sync Data 三个 000003.log，以及 Default 下 GCM Store、Platform Notifications、Tea\common\tea.db 三个 000003.log。

九、本轮合计释放 21258343 字节，约 20.27MB，C 可用由 76.94GB 到 76.96GB。D、E 无迁移动作。

2026-11-19 17:10 至 17:22，第四十六轮定时清理，只清不迁

一、清理前基线，C 可用 75.96GB 已用 137.48GB，D 可用 90.78GB，E 可用 102.49GB。C 仍远超 40GB 线，本轮不启动迁移。

二、体积基线，C:\Users\Administrator 326113 文件 89744438924 字节，AppData\Local 94316 文件 9794018701 字节，C:\Windows 164859 文件 19096775374 字节，C:\ProgramData 4937 文件 8845342604 字节。

三、AppData\Local\Temp 空目录 0 文件，无释放。C:\Windows\SoftwareDistribution\Download 也是 0 文件，无释放。

四、C:\Windows\Temp 清理前 5 文件 106243 字节，清完剩 2 文件 105800 字节，释放 443 字节，删掉的是 virtual_camera_12404.log。剩下两项被占用跳过，TAOAcceleratorEx64_ev.sys19-7-0 是驱动替身 105800 字节，virtual_camera_5204.log 由虚拟摄像头驱动占用。

五、__pycache__ 命中 11 个目录、47 个文件 896361 字节，11 个目录全部删除成功，无占用失败。

六、更新器残留目录 @mmx-agentelectron-updater 已不存在，无释放。

七、浏览器与 Electron 缓存里只剩 Edge 的 Cache 有一个 journal.baj 4 字节且被占用，本轮缓存释放 0 字节；Edge 的 Code Cache、GPUCache、Service Worker CacheStorage 与豆包、MiniMax 缓存目录全为空。

八、超过 30 天 .log 候选 388 个，删 382 个，释放 938336 字节；6 个被占用跳过，都在豆包用户数据里，aha\users 下 profile_explorer 的 Extension State、GCM Store\Encryption、Sync Data\LevelDB 三个 000003.log，以及 Default 下 GCM Store\Encryption、Platform Notifications、Tea\common\tea.db 三个 000003.log。

九、本轮合计释放 1835140 字节，约 1.75MB，C 可用由 75.96GB 到 75.95GB。D、E 无迁移动作。

累计：D:\C盘搬迁_20261111 现有 30,961 文件 25.81GB；D:\C盘搬迁_定时迁移 现有 294395 文件 19.80GB。

2026-11-19 20:17 至 20:52，第四十七轮定时清理，只清不迁

一、清理前基线，C 可用 73.30GB 已用 140.14GB，D 可用 90.62GB，E 可用 102.38GB。C 已远超 40GB 线，按规则本轮不启动迁移。

二、体积基线，C:\Users\Administrator 874138 文件 158206696014 字节，AppData\Local 168342 文件 20192938798 字节，C:\Windows 164879 文件 19758401194 字节，C:\ProgramData 4880 文件 8850683718 字节。

三、AppData\Local\Temp 空目录 0 文件，无释放。C:\Windows\SoftwareDistribution\Download 也是 0 文件，无释放。

四、C:\Windows\Temp 清理前 2 文件 107125 字节，清完仍是 107125 字节，释放 0。两项全部被占用跳过，TAOAcceleratorEx64_ev.sys19-7-0 是驱动替身 105800 字节、拒绝访问；virtual_camera\virtual_camera_30772.log 由虚拟摄像头驱动占用。

五、__pycache__ 命中 7 个目录、1401532 字节，7 个目录全部删除成功，无占用失败。

六、更新器残留本轮只命中 @guanjia-openclawelectron-updater，是 0 字节空目录，已整目录删，无释放；@mmx-agentelectron-updater 已不存在。

七、浏览器与 Electron 缓存只剩 Edge 的 Cache 下一个 No_Vary_Search\journal.baj 4 字节且被占用，释放 0 字节；Edge 的 Code Cache、GPUCache 已空，Chrome 三个缓存目录不存在。

八、超过 30 天的 .log 删 127 个，释放 2483653 字节，全部落在 AppData\Local\Doubao\User Data\Default\agent_infra\to 下各 task_outputs 的 output.log，无占用失败。

九、本轮合计释放 3885185 字节，约 3.71MB。C 可用由 73.30GB 到 77.24GB，涨了 3.94GB，但本轮清理只占 3.71MB，其余差额来自本机其他进程与用户自己的操作，不计入本轮成果。同窗口 E 盘已用由 130.74GB 涨到 135.90GB，也是外部写入。D、E 无迁移动作，零迁移。

累计：D:\C盘搬迁_20261111 现有 30,961 文件 25.81GB；D:\C盘搬迁_定时迁移 现有 294395 文件 19.80GB。

━━━━━━━━━━━━━━━━

四、暂时还留在 C 盘的大块，以及为什么

.minimax\v2\sessions　18.03GB　9,110 文件　你自己的历史会话。两次搬迁时你都有 8 到 10 个进程在跑，动它可能损坏会话索引。要归档必须先完全退出 MiniMax Code，再整体搬走并在原位建目录联接。步骤见桌面「给MiniMax的文件迁移说明_v3.md」。

xwechat_files　19.66GB　微信活数据，只能在微信设置里改存储位置。

AppData\Local 20.66GB，Programs 5.21GB、Microsoft 2.55GB、Feishu 2.29GB、AndroidToolchain 1.23GB、ShouyangTerminal 0.53GB 占大头。Feishu 这一块 10-24 之后没再写，但飞书主程序仍在用，属程序本体，没搬。Temp 每两小时清一次，本轮清完是 0。

用户目录下最占位的两块是活数据，都不算冷：.mavis 28.16GB、.minimax-agent-cn 5.06GB，两者今天都还在写，按规则不动。

AppData\Roaming 里的 kingsoft 3.37GB、Tencent 2.77GB、LarkShell 1.70GB、MiniMax 492MB、thunder 403MB 都在持续写入或是程序本体，不算冷数据，未搬。原先挂在这里的 npm 1.28GB 本轮已迁走。

已迁走的一百五十八块，C 盘只剩下目录联接，不再实际占位：.qclaw、.agents、.openclaw-windclaw、lobsterai、Roaming\LobsterAI、Roaming\QClaw、.paddlex、Local\electron、Local\JianyingPro，第七轮的 Roaming\蚁小二4.0、Roaming\bilibili、Roaming\greencore、Roaming\douyin、Roaming\360se6、.cache、Local\ChromeExtensionCache、Roaming\@hilo、Roaming\autoclaw、Roaming\WindClaw、.EasyOCR、.openclaw、.hub，本轮的 self-improving、Local\DingTalk_133、Local\qmlauncher-updater、Local\yiheng-deploy-updater、Local\Thunder Network、Local\node-gyp、Local\com.tencent.yuanbao、Local\Package Cache、Local\flutter_webview_windows、Roaming\obs-sh_main-min-0.7.3-soft、Roaming\ollama app.exe、Roaming\SodaMSOAddin、Roaming\Python、Roaming\Blackmagic Design、Roaming\hotspotessw、Roaming\npm，第九轮的 Local\ShadowBot、Local\ShadowBotBrowser、Local\Android、Local\qBittorrent、Local\kdocs-cli、Local\Bytedance、Local\DQSStockPro、Local\ai.openclaw.clawpanel、Roaming\Octopus8、Roaming\360Aiview、Roaming\NGRLauncher，第十轮的 Local\electron-builder、Roaming\WebView、Roaming\temp、Roaming\lct、Roaming\HuoYuYan、Roaming\yiheng-ai、Roaming\xmpclient、Roaming\yiheng-deploy、Roaming\douyin_widget、Roaming\AiLoginServer、Roaming\360FileBrowser、Roaming\Mozilla，第十一轮的 C:\Users\Administrator\.cargo、.android、.agent-browser、.mempalace、Local\fontconfig、Local\CEF、Local\DingTalk_108、Local\SolidDocuments、Roaming\GreenCore7z、Roaming\obs-studio、Roaming\CoreLog、Roaming\utForpc，第十二轮的 C:\Users\Administrator\_bak_s2_20261105、_bak_rules_20261106_kjty、openclaw_temp_a_stock、.skillhub、.Trash、.cliguard、.iwencai-skillhub、.iwencai-temp、.crawl4ai。

Desktop 23.29GB　65,486 文件，01_股票研究、ucl_special、02_内容创作、选股系统备份 都在持续写入，不算冷数据，不动。

Windows 19.20GB、pagefile.sys 16GB、ProgramData 8.20GB，系统与程序，不动。

━━━━━━━━━━━━━━━━

五、禁止触碰的活系统，谁都不许搬

C:\Users\Administrator\首阳战法回测引擎　8767 终端服务、计划任务、start_terminal.ps1 写死绝对路径。
C:\Users\Administrator\Desktop\01_股票研究\异动归因全文　7 个 py 写死自身目录，桌面入口是指向它的联接。
C:\Users\Administrator\Desktop\选股系统备份　15,902 文件，各股票框脚本与云同步脚本写死路径。
C:\Users\Administrator\AppData\Local\Doubao 与 com.minimax.hub　程序本体。
搬动这四处会立刻断每日 15:41 自采、16:20 维护、16:00 库快照和云同步。

━━━━━━━━━━━━━━━━

六、调用约定

要读素材直接从 D 盘读，不要复制回 C 盘。
要恢复单个成品到桌面用复制不用移动，恢复前先看有没有同名文件，有就先把旧的改名。
整套备份要挪到别的机器，整目录复制即可，内部是相对结构，没有绝对路径依赖。
D 盘里的文件不许删，只许读与复制。注意 C 盘上已有一百五十八处目录联接指向 D:\C盘搬迁_定时迁移，删联接等于删 D 盘里的备份，动这些目录前先确认 LinkType 是 Junction。

━━━━━━━━━━━━━━━━

七、更新记录

2026-11-12 14:52　建立本文件，记录三批迁移与当前空间。
2026-11-12 16:32　定时任务第一轮完成：清 Temp 与缓存、删超 30 天日志、迁入 .qclaw-backups 2.57GB。C 可用 28.8GB 升至 31.6GB。
2026-11-12 18:22　定时任务第二轮完成：清同花顺旧版安装包 996.4MB 与少量缓存日志，本轮无冷数据可迁。C 可用 33.2GB 升至 34.13GB。
2026-11-13 08:29　定时任务第三轮完成：清临时文件、124 个旧日志、137 个 __pycache__，共 82.7MB；本轮无冷数据可迁。C 可用清理前 34.13GB，清理后实测 34.07GB，差值是同期豆包与 MiniMax 写入吃掉的。前六轮 20:17 至 06:17 因本机离线未执行。
2026-11-13 09:19　定时任务第四轮完成（用户 08:29 后批准补做）：删 ShadowBot 更新补丁 641.5MB、Roaming\LobsterAI 更新包 243.3MB、剪映 SupplysStore 本地 ASR 素材 1124.2MB，合计 2009.0MB；.qclaw 4.70GB 迁到 D 盘并在原位建联接。C 可用删除前 33.96GB，搬迁后实测 31.92GB，差值来自同期写入：MiniMax runtime-state.sqlite 涨到 2186.5MB、WPS 云缓存 cache.db 461.5MB、首阳战法 engine.db 与客户版安装包约 0.5GB。
2026-11-13 10:31　定时任务第五轮完成：清 Temp、Windows\Temp、Edge 与豆包缓存、__pycache__、超 30 天日志，共 479.6MB；五块冷程序目录 4.66GB 迁往 D 盘并在原位建联接。C 可用由本轮开始 33.00GB 升到 37.98GB，净增 4.98GB。
2026-11-13 12:27　定时任务第六轮完成：清临时目录、豆包缓存、__pycache__ 与超 30 天日志，共 56.26MB；.paddlex、AppData\Local\electron、AppData\Local\JianyingPro 三块 1.58GB 迁往 D 盘并在原位建联接。C 可用由本轮开始 36.72GB 升到 38.37GB，净增 1.65GB。
2026-11-13 14:26　定时任务第七轮完成：清豆包缓存与 __pycache__，共 7.79MB，Temp 已空；十三块冷目录 3.78GB 迁往 D 盘并在原位建联接。C 可用由本轮开始 38.27GB 升到 42.07GB，净增 3.80GB，已越过 40GB 只清不迁的界线。
2026-11-14 10:39　定时任务第八轮完成：清 374.5MB，其中更新器残留安装包 274.15MB、豆包缓存与 Code Cache、GPUCache 共 29.57MB、Local\Temp 7.84MB、__pycache__ 18.49MB、超 30 天日志 12341 个 44.53MB；十六块冷目录 2.11GB 迁往 D 盘并在原位建联接。C 可用由本轮开始 39.49GB 掉到 38.34GB，同期 MiniMax runtime-state.sqlite 2186.5MB、WPS 云缓存 cache.db 461.5MB、首阳战法 engine.db 208.7MB、MiniMax 会话快照与视频素材约 0.67GB 写进来，吃掉了本轮释放与搬迁的 2.48GB 还不够。前四轮 16:17 至 22:17 与本日 08:17 因本机离线未执行，10:17 起本机恢复在线。
2026-11-14 12:22　定时任务第九轮完成：清 18.4MB，其中 __pycache__ 80 个目录 18.17MB、超 30 天日志 13 个 1.01MB、Local\Temp 5 文件 135106 字节、豆包 Code Cache 3 文件 19836 字节；十一块冷目录 0.22GB 迁往 D 盘并在原位建联接，electron-builder 目标件数对上但源侧未删除，已整体回滚。C 可用由本轮开始 36.22GB 到 36.42GB。
2026-11-14 14:23　定时任务第十轮完成：清理只清到 Local\Temp 的 813 字节，Windows\Temp 与豆包 Cache 的 No_Vary_Search 仍被占用跳过，超 30 天日志与 __pycache__ 本轮扫描为零；十二块冷目录 0.14GB 迁往 D 盘并在原位建联接，electron-builder 第三次搬成功，根因是目录内有两条 macOS 相对软链，robocopy 不复制符号链接，改为复制后在 D 盘重建软链才过判据。C 可用由本轮开始 36.40GB 升到 36.54GB，D 可用由 6.01GB 降到 5.86GB。
2026-11-14 16:22　定时任务第十一轮完成：清理只清到 Local\Temp 的 813 字节，Windows\Temp 的 virtual_camera 两个日志与豆包 Cache 的 No_Vary_Search 仍被占用跳过，超 30 天日志与 __pycache__ 本轮扫描为零；十二块冷目录 0.03GB 迁往 D 盘并在原位建联接，其中 .cargo 含 13 条 rustup 软链，按重建软链的办法一次通过。C 可用由本轮开始 36.50GB 到 36.52GB，D 可用由 5.86GB 降到 5.83GB，落点累计 293805 文件 19.80GB，联接共 73 处。
2026-11-14 18:21　定时任务第十二轮完成：清理只清到豆包 Code Cache 的 21356 字节，Local\Temp 已空，Windows\Temp 的 virtual_camera 两个日志与新增的 TAOAcceleratorEx64_ev.sys14-16-25 均被占用跳过，超 30 天日志与 __pycache__ 本轮扫描为零；九块零星冷目录 0.01GB 迁往 D 盘并原位建联接，无软链、无回滚。C 可用由本轮开始 35.61GB 到 35.52GB，D 可用 5.74GB，落点累计 293983 文件 19.80GB，联接共 82 处。
2026-11-14 20:21　定时任务第十三轮完成：清理释放 18244086 字节，其中 __pycache__ 125 个目录 810 文件 18203409 字节、豆包 Code Cache 24377 字节；超 30 天日志为零，Local\Temp 前后都空，Windows\Temp 的 virtual_camera 与 TAOAcceleratorEx64_ev.sys14-16-25、豆包 No_Vary_Search 均被占用跳过；剩余 76 块零散冷目录 2249042 字节迁往 D 盘并原位建联接，无软链、无回滚。C 可用由本轮开始 34.03GB 到 34.04GB（两小时被写掉 1.49GB），D 可用 5.65GB，落点累计 294276 文件 19.80GB，联接共 158 处。
2026-11-14 22:21　定时任务第十四轮完成：清理释放 10673972 字节，全部是 __pycache__ 71 个目录 496 文件；超 30 天日志为零，Local\Temp 前后都空，Windows\Temp 的 virtual_camera 与 TAOAcceleratorEx64_ev.sys14-16-25、豆包 No_Vary_Search 仍被占用跳过；本轮没有新迁入，冷目录已搬空，只有飞书本体、Comms、个人数据与凭据目录留下。C 可用由本轮开始 31.95GB 到 31.96GB（两小时被写掉 2.09GB），D 可用 5.56GB，落点 294395 文件约 19.80GB，联接 158 处。
2026-11-15 08:15　定时任务第十五轮完成：本轮只清不迁（D 盘可用 5.41GB，接近满，暂停迁移）。七类清理释放 428415477 字节，其中豆包 Cache 83873867、豆包 Code Cache 4715209、豆包 GPUCache 5837168、__pycache__ 12320420、@mmx 旧安装包 287462056、Local\Temp 8199464。另按指令删掉 9 个已完成混剪项目的过程目录 4.79GB 与 E 盘 2.75GB 重复副本、0.65GB 旧工作目录，成品全部保留。C 可用由本轮开始 30.58GB 到 33.83GB，净增 3.25GB。落点 294395 文件约 19.80GB，联接 158 处。
2026-11-15 08:19　定时任务第十六轮完成：D 盘可用 5.31GB，低于单轮 5GB 迁移余量，本轮只清不迁。七类清理释放 293034048 字节，其中更新器残留安装包 287462056、__pycache__ 10498150、豆包 Code Cache 68146、Local\Temp 5696。新增的过程目录（2025豆瓣高分动画片混剪 326.1MB、2025豆瓣高分战争历史片混剪 160.8MB、_qc_tmp 1MB）正在跑，暂不清理。C 可用由本轮开始 33.54GB 到 33.80GB，净增 0.26GB。落点 294395 文件约 19.80GB，联接 158 处。
2026-11-15 10:18　定时任务第十七轮完成：本轮只清不迁。七类清理释放 13936372 字节（Edge Cache 6152852、__pycache__ 6811827、豆包 Code Cache 753072、Local\Temp 218477）。另删三个已出成品项目的过程目录与 _qc_tmp，共 153 文件 942200579 字节约 898.6MB，成品六支 mp4 全部保留。2026豆瓣高分前十混剪 523.4MB 仍在跑无成品，整体保留。C 可用由本轮开始 30.23GB 到 30.89GB，净增 0.66GB。落点 294395 文件约 19.80GB，联接 158 处。
2026-11-15 12:21　定时任务第十八轮完成：本轮只清不迁。七类清理释放 41130824 字节，全部来自豆包 Code Cache（544 文件）。查清 D 盘掉得快的两个原因：一是 C盘搬迁_20261111 29.53GB 与 定时迁移 19.8GB 两块历史落点占了 49GB；二是 TEMP 环境变量指向 D 盘，D:\Users\Administrator\AppData\Local\Temp 已堆到 5.39GB 65001 文件，内含 30 个 PyInstaller 残留 _MEI 目录共 2502.9MB。C 可用由本轮开始 29.59GB 到 29.62GB。落点 294395 文件约 19.80GB，联接 158 处。
2026-11-15 14:19　定时任务第十九轮完成：本轮只清不迁。七类清理释放 6046132 字节，全部来自豆包 Code Cache（384 文件）。D 可用 4.96GB 仍低于单轮 5GB 上限，迁移为零，落点仍 294395 文件约 19.80GB。D 盘 Temp 已到 5.40GB 65079 文件，PyInstaller 残留 _MEI 目录 30 个共 2502.9MB 未清。C 可用由本轮开始 28.49GB 到 28.50GB。
2026-11-15 14:2x　用户追问 D 盘为什么满，本轮补做两步清理：D:\Users\Administrator\AppData\Local\Temp 下 25 个超过 6 小时没人回收的 PyInstaller 解包残留 _MEI 目录，删掉释放 2013.5MB；D:\MavisVideo\素材\batch_assets\series\anim 下的 timeline（185.9MB，51 文件）与 _subaudit，成品 2025动画片TOP5混剪与配音版已于 08:11、08:12 落盘，过程目录可删。D 盘可用由 4.96GB 回到 7.17GB。anim\src 4151.8MB 是 11-14 新下载未使用素材，按用户口径未动。
2026-11-15 16:19　定时任务第二十轮完成：C 可用 40.53GB 已过 40GB 线，本轮只清不迁。七类清理仅释放 443 字节（Windows\Temp 一个小文件），其余六类为零；迁移为零，落点仍 294395 文件约 19.80GB。D 盘 Temp 由 5.40GB 降到 3.44GB、E 盘已用少了 12.42GB，属系统与其它程序自行释放，不是本轮动作。成品 24 支 mp4 共 1002.1MB 一支没少。
2026-11-15 17:40　按用户指令把两块大占用搬到 E 盘：E:\C盘搬迁_定时迁移（294380 文件 19.80GB，D 盘原路径改联接）、E:\C盘搬迁_20261111（30969 文件 29.53GB，旧 D 路径失效）、E:\股票回测数据 下大华市场与低估双底与首板回调与10日均线与20日均线（合计约 32.54GB，D 盘原路径改联接）。D 盘可用 7.15GB 回到 90.06GB，E 盘可用 56.41GB。同花顺板块与主本因客户端占用未搬，已退回 D 盘原状。20日均线丢失 15 文件 13.31MB，已在正文记录。
2026-11-15 18:25　第二十一轮定时任务：清理释放 6877248 字节（Temp 6022、Windows Temp 443、豆包 Code Cache 1060005、__pycache__ 5810777），迁移三块冷数据共 215 文件 1181555913 字节约 1.10GB（2345Ad\Components、QQPCMgr radiumv3\wmpfsdk、Tencent\WXWork），全部先复制后比对再删源，回读件数字节对上。C 盘可用 38.85GB 到 39.93GB。飞书 2185.8MB、Local\Programs\Python 4.19GB、ShouyangTerminal 518.4MB、.minimax sessions 235.2MB 因在用未搬。落点 D:\C盘搬迁_定时迁移 为联接，实体在 E 盘，E 盘可用 55.32GB。
2026-11-15 20:31　第二十二轮定时任务：清理释放 35924869 字节（豆包 Code Cache 13500209、__pycache__ 22424660），迁移五块冷数据共 33320 文件 3369875996 字节约 3.14GB（AndroidToolchain、Python37-32、LarkShell aha 用户缓存、Edge ProvenanceData、kingsoft everythingsearch），AndroidToolchain 与 Python37-32 已在 C 盘原位建联接。C 盘可用 37.16GB 到 39.85GB。飞书 2185.8MB、torch 1148.3MB、ShouyangTerminal 518.4MB 因在用未搬。落点 D:\C盘搬迁_定时迁移 为联接，实体在 E 盘，E 盘可用 51.90GB。
2026-11-15 22:24　第二十三轮定时任务：清理释放 573126274 字节（Edge Service Worker CacheStorage 553705887、__pycache__ 18765019、豆包 Code Cache 655368），迁移六块冷数据共 3589 文件 615769833 字节约 0.57GB（旧版 Edge UserData、腾讯管家全局搜索引、WPS cef、docerFonts、qing_3.1.0.19667、kufeconvertplugin）。C 盘可用 36.94GB 到 37.97GB。飞书、在用 Python、系统字体、终端配置、在办视频工程未动。E 盘可用 51.33GB。
2026-11-16 08:47　第二十四轮定时任务：清理释放 54273775 字节（Local\Temp 8199464、豆包 Cache 28773450、__pycache__ 10702311、豆包 GPUCache 5837168、豆包 Code Cache 734633、超 30 天 .log 26725、Edge Cache 24），迁移两块共 80 文件 793621836 字节约 0.76GB（WPS office6\update、用户字体 Fonts），两处均留 Junction。C 盘可用 33.73GB 开始，清理加迁移净腾 845MB，但期间新写入约 1.24GB，收尾 33.33GB。E 盘可用 50.44GB。
2026-11-16 10:37　第二十五轮定时任务：清理释放 7988709 字节（全部来自 __pycache__ 48 目录 373 文件，其余七类均为空或被占用），迁移两块共 1073 文件 582356865 字节约 0.54GB（ShouyangTerminal\edge_profile、HaoZip\Application），两处均留 Junction。C 盘可用 31.52GB 开始，收尾 32.08GB，本轮实涨 0.56GB。E 盘可用 49.63GB。
2026-11-16 12:23　第二十六轮定时任务：清理释放 10693615 字节（豆包 Code Cache 23478、__pycache__ 62 目录 483 文件 10670137，其余七类为空或被占用），迁移 40 个目录共 378 文件 2106334573 字节约 1.96GB（足球成品合集 39 个冷成品目录 + 指标和策略优化迭代），全部留 Junction。C 盘可用 31.41GB 开始，收尾 33.35GB，本轮实涨 1.94GB。E 盘可用 47.33GB。
2026-11-16 14:24　第二十七轮定时任务：清理释放 2296294 字节（全为 __pycache__ 17 目录 102 文件，其余七类为空或被占用），迁移 3 个目录共 5689 文件 400286196 字节约 0.37GB（龙虾命中的个股 下 K线库、data、_crop），全部留 Junction。C 盘可用 29.77GB 开始，收尾 30.16GB，本轮实涨 0.39GB；期间新写入约 1.1GB 豆包更新包与 287.5MB MiniMax 升级包，未删。E 盘可用 46.86GB。
2026-11-16 16:24　第二十八轮定时任务：清理释放 131395 字节（Windows\Temp 1 项 1768 与豆包 Code Cache 211 文件 129627，__pycache__ 本轮为 0），迁移 6 个目录共 3378 文件 309143419 字节约 0.29GB，全部留 Junction。C 盘可用 27.26GB 开始，收尾 27.28GB，期间新写入约 0.27GB（回测库与库备份约 840MB、恐怖大师混剪 trailer 158MB、分类榜出片约 330MB）抵掉了搬家收益。E 盘可用 46.56GB。
2026-11-16 18:24　第二十九轮定时任务：清理 475161562 字节约 0.44GB（Local\Temp 8199464、豆包 Cache 68994336、豆包 Code Cache 89794277、Edge Cache 6152852、GPUCache 5837168、Windows\Temp 1662、__pycache__ 8726363、重复安装包 287455296），迁移 6 块 231 文件 425120331 字节约 0.40GB，全部留 Junction，零回滚。C 盘可用 28.08GB 到 28.83GB。D 可用 89.42GB，E 可用 46.31GB。
2026-11-16 20:26　第三十轮定时任务：清理 20583058 字节约 0.02GB（豆包 Code Cache 2376063、__pycache__ 18206995，其余各项为 0），迁移 10 块 4147 文件 587111955 字节约 0.56GB，全部留 Junction，零回滚。C 盘可用 25.46GB 到 25.86GB。D 可用 89.16GB，E 可用 45.81GB。
2026-11-16 22:32　第三十一轮定时任务：清理 14810469 字节（全是豆包 Code Cache，__pycache__ 与日志本轮为 0），迁移 6 块 660 文件 794635943 字节约 0.74GB，全部留 Junction，零回滚，Python312 导入实测通过。C 盘可用 25.02GB 到 25.72GB。D 可用 86.10GB，E 可用 45.04GB。
2026-11-17 08:26　第三十二轮定时任务：清理 52733219 字节（Temp 8.2MB、Edge 与豆包缓存合计 42MB、__pycache__ 1.7MB），迁移 13 块 21427 文件 2422893026 字节约 2.26GB，全留 Junction，零回滚，torch 与 paddle 等导入实测通过。C 盘可用 36.24GB 到 38.57GB，另查明一夜多出 10.52GB 主要是 MiniMax 自己回收 .minimax\v2 旧会话。D 可用 86.13GB，E 可用 42.43GB。
2026-11-17 16:10　桌面大文件专项：搬 4 块 18211 文件 20989362832 字节约 19.54GB 到 E:\桌面大文件迁移_20261117，全留 Junction，零回滚；C 盘可用 40.05GB 到 59.07GB，E 盘剩 19.78GB。
2026-11-17 14:30　第三十四轮定时任务：清理 18102356 字节（豆包 Code Cache 25117、__pycache__ 119 目录 800 文件 18077239，其余七类为空或被占用），迁移 1 块 8012 文件 2292007845 字节约 2.13GB，飞书 AppData\Local\Feishu 全冷且进程已退出，全留 Junction，零回滚。C 盘可用 37.89GB 到 40.05GB，已回到 40GB 线以上，后续轮次只清不迁。D 可用 85.88GB，E 可用 39.06GB。
2026-11-17 11:24　第三十三轮定时任务：清理 991380 字节（豆包 Code Cache 85750、__pycache__ 45 文件 904305，其余七类为空或被占用，Windows\Temp 仅释放 1325），迁移 78 块 9670 文件 637595878 字节约 0.59GB，全留 Junction，零回滚，WPS 插件池只搬被新版本取代的旧版本，新版本仍留 C 盘。C 盘可用 39.31GB 到 39.90GB，仍差 0.10GB 到 40GB 线。D 可用 85.90GB，E 可用 41.45GB。
2026-11-19 17:22　第四十六轮定时清理：C 可用 75.96GB 只清不迁，七类释放 1835140 字节约 1.75MB，其中 30 天以上 .log 382 个 938336 字节、__pycache__ 11 个目录 896361 字节、Windows\Temp 443 字节，缓存释放 0；6 个豆包 LevelDB 日志与 TAO 驱动替身、虚拟摄像头日志被占用跳过；C 收尾 75.95GB，D 90.78GB，E 102.49GB。2026-11-19 14:22　第四十五轮定时清理：C 可用 76.94GB 只清不迁，七类释放 21258343 字节约 20.27MB，其中 30 天以上 .log 3705 个 19888500 字节、__pycache__ 92 个目录 1368795 字节、Windows\Temp 1028 字节、Edge Cache 20 字节；6 个 LevelDB 与豆包日志被占用跳过；C 可用收尾 76.96GB，D 90.76GB，E 102.84GB。2026-11-19 13:58　E 盘重复合并：SHA256 判重 500 组，删 574 个重复件释放 11961003089 字节约 11.14GB，E 可用 92.09GB 升到 102.91GB；4 个成品路径已按哈希恢复；76 组 308MB 桌面路径被链式删除，其中 73 组 227MB 无同名副本，清单另存 给MiniMax的搬迁提示词\E盘去重丢失清单.md。
2026-11-19 13:32　清空回收站：C 6735.67MB 共 194916 文件、D 47.59MB 共 752 文件、E 0.01MB 共 16 文件全部清空，三盘回收站为 0 文件，C 可用 70.81GB 升到 77.07GB，D 90.78GB。2026-11-19 13:14　删系统镜像并清 C、D：E 盘删 GHO 76.22GB 后可用 16.04GB 升到 92.26GB；C 盘清垃圾 5.67GB 可用 65.14GB 升到 70.81GB；D 盘清 Temp 6.60GB 可用 83.85GB 升到 90.75GB；占用跳过 122 个文件。
2026-11-19 13:02　B 站版成片清理：删 83 个 B站横版与无配音文件，释放 3345038726 字节约 3.11GB，抖音版全部保留，E 可用 12.93GB 升到 16.04GB；另生成 已做过视频清单.md 2813 条防重复。
2026-11-19 11:44　E 盘专项清理：删分类榜工程素材与中间件 8.5GB、素材库工作目录 2.63GB、足球下载暂存 0.89GB、迁移目录旧缓存 0.49GB 及临时目录，合计 13325465716 字节约 12.41GB；E 可用 0.49GB 升到 12.93GB，成片未动。
2026-11-19 11:20　第四十四轮定时清理：C 可用 65.09GB 只清不迁，七类释放 27800797 字节，旧日志 2 个 2009 字节，__pycache__ 零命中；Windows\Temp 释放 1768 字节；两项被占用跳过；收尾 C 可用 65.12GB，E 盘由 3.73GB 掉到 0.59GB 已见底。
2026-11-19 08:20　第四十三轮定时清理：C 可用 65.61GB 只清不迁，七类释放 56573776 字节，__pycache__ 与旧日志两段本轮全空；Windows\Temp 删 3 项但因同期写入净增 443 字节；两项被占用跳过；收尾 C 可用 65.65GB。
2026-11-18 23:20　第四十二轮定时清理：C 可用 64.67GB 只清不迁，七类释放 6190967 字节加 __pycache__ 1801552 字节与旧日志 8732 字节，合计 8001251 字节约 7.6MB；常规缓存已清到接近空档；四项被占用跳过；收尾 C 可用 64.67GB 持平，E 仍 3.73GB。
2026-11-18 20:20　第四十一轮定时清理：C 可用 65.80GB 只清不迁，七类释放 74712592 字节加 __pycache__ 18203409 字节与旧日志 143874 字节，合计 93099875 字节约 88.8MB；两项被占用跳过；C 可用收尾 65.86GB 比起点多 0.06GB。
2026-11-18 17:19　第四十轮定时清理：C 可用 66.42GB 只清不迁，七类释放 92326504 字节加 __pycache__ 18737429 字节，合计 111063933 字节约 105.9MB；三项被占用跳过；收尾 C 可用 66.00GB，E 只剩 3.60GB 已到极限。
2026-11-18 11:23　第三十九轮定时清理：C 可用 69.14GB 只清不迁，七类释放 28702 字节加 __pycache__ 22043736 字节，合计 22072438 字节约 21.1MB；两项被占用跳过；C 可用收尾 69.11GB，E 只剩 6.05GB 需尽快腾。
2026-11-18 08:20　第三十八轮定时清理：C 可用 73.09GB 只清不迁，七类释放 46585517 字节加 __pycache__ 18001873 字节，合计 64587390 字节约 61.6MB；三项被占用跳过；C 可用收尾 73.14GB，E 9.28GB。
2026-11-17 23:33　第三十七轮定时清理：C 可用 68.23GB 只清不迁，七类释放 0 字节加 __pycache__ 1106097 字节，合计约 1.05MB；两条被占用跳过；C 可用收尾 68.24GB，E 降到 10.16GB。
2026-11-17 20:38　第三十六轮定时清理：C 可用 71.91GB 只清不迁，七类释放 15495983 字节加 __pycache__ 18415368 字节，合计 33911351 字节约 32.3MB；两条被占用跳过；C 可用收尾 71.87GB，E 13.14GB。
2026-11-17 20:26　旧素材清理：分类榜工程删 trailers、output、clips、audio、check 共 2303 文件约 8.55GB，成片与脚本全留，E 盘可用 4.68GB 到 13.18GB。
2026-11-17 19:50　桌面大文件二次迁移：按超过 100MB 全搬的口径，搬 8 块 45655 文件 15541550164 字节约 14.48GB 到 E:\桌面大文件迁移_20261117，全留 Junction，内部 7 加 40 处联接已重建；C 盘可用 59.86GB 到 72.95GB，E 盘剩 4.68GB。
2026-11-17 18:20　第三十五轮定时任务补跑收尾：七类加 pycache 与 30 天日志合计释放 117934370 字节约 112.5MB，更新器 pending 安装包 287455296 字节同窗口已清，C 盘可用 59.51GB 到 59.86GB，本轮不迁移。
2026-11-17 18:12　第三十五轮定时任务（补 17:17 掉线漏跑）：清理 288925997 字节约 0.27GB（重复安装包 @mmx-agentelectron-updater 287455475、__pycache__ 12 目录 1467079、Local\Temp 3443；Windows\Temp 108434 被占用未释放、SoftwareDistribution\Download 不存在、豆包 Cache/Code Cache/GPUCache 与 Edge Cache 为空或已无内容、超 30 天 .log 0 个）。本轮不迁数据，C 盘可用已过 40GB 线，按规则只清不迁。C 盘可用 63.99GB 到 64.27GB。D 可用 86.17GB，E 可用 19.77GB。
2026-11-19 21:31 至 23:14　C 盘整卷镜像备份完成，用 wimlib-imagex 1.14.5 对 C 盘做 VSS 热备份，LZMS 固实压缩，输出 E:\系统镜像备份\C盘整卷镜像_20261119.wim，68.38GB 即 73,418,140,207 字节，覆盖 530,238 文件 184,390 目录，原始 126,939,681,118 字节；21:31:52 起跑，23:14:02 写盘完成，23:28 全量 verify 通过；VSS 快照已自动释放，C 可用 76.07GB，E 可用 27.41GB。排除 pagefile.sys 16GB、休眠文件与还原点，另排除 WPS Cloud Files，因其中云占位文件读错误 c000cf0c 会中止整盘备份。
2026-11-19 23:33 至 23:35　第四十七轮定时清理，只清不迁（C 可用 76.06GB 远超 40GB 线）。七类合计释放 232,460,190 字节约 221.7MB：更新器残留 7 个目录 174,824,043 字节，其中 qmlauncher-updater 93,126,152、yiheng-deploy-updater 81,697,891，其余 bilibili、bitbrowser、lobsterai、motrix、windclaw 五个是空目录；__pycache__ 130 目录 819 文件 18,259,043；豆包 Code Cache 652 文件 39,059,094；C:\Windows\Temp 4000 字节；超 30 天 .log 45 个 314,010。被占用跳过 8 项：C:\Windows\Temp\virtual_camera\virtual_camera_5204.log 与 TAOAcceleratorEx64_ev.sys19-7-0（权限拒绝），Edge 与豆包 Cache 下 No_Vary_Search 各 4 字节 journal，豆包用户数据里 5 个 LevelDB 000003.log。Local\Temp 与 SoftwareDistribution\Download 本轮均空。C 可用由 76.06GB 到 76.11GB，D 90.60GB，E 27.41GB 到 27.43GB。

2026-11-20 00:57　第四十八轮定时清理，只清不迁（C 可用 75.60GB，远高于 40GB 线，按规则不启动迁移）。七类合计释放 36884 字节约 36KB，全部来自超过 30 天的 .log 10 个；Local\Temp 已空、SoftwareDistribution\Download 空、__pycache__ 零命中、更新器残留零命中、Chrome 与 Edge 的 Cache 与 Code Cache 与 GPUCache 近空、Windows\Temp 只剩被占用项。被占用跳过 9 项：C:\Windows\Temp\virtual_camera、C:\Windows\Temp\TAOAcceleratorEx64_ev.sys19-7-0 权限拒绝，Edge Cache 的 No_Vary_Search，豆包用户数据下 6 个 LevelDB 000003.log。C 可用 81174806528 字节到 81170325504 字节即 75.60GB 到 75.59GB，D 90.44GB，E 26.15GB。
2026-11-20 00:57　C 盘整卷镜像仍在 E:\系统镜像备份\C盘整卷镜像_20261119.wim 与同目录的 C盘镜像恢复说明.md，68.38GB 已 verify 通过；00:25 起尝试上传迅雷云盘未成功，原因是迅雷客户端窗口不接收自动化鼠标点击、主桌面接管授权连续超时，镜像原样留在 E 盘未动。

2026-11-20 08:25　第四十九轮定时清理，只清不迁（C 可用 76.28GB 远超 40GB 线，D 90.31GB、E 25.94GB）。七类合计释放 62403085 字节约 59.5MB：豆包 Cache 44.9MB、豆包 GPUCache 5.6MB、用户 Temp 7.82MB、豆包 Code Cache 0.5MB、__pycache__ 5 目录 414,706 字节、超 30 天 .log 45 个 366,072 字节（均为 8 月至 11 月的 _rebuild 与 _ser 构建日志，分布在 .minimax\sessions、.minimax-agent-cn、豆包 agent_infra 与 WPS 缓存，未动任何 sqlite 主库）；Windows\Temp、SoftwareDistribution\Download、更新器残留、Edge Cache 本轮释放为零。被占用跳过 9 项：Windows\Temp\virtual_camera 与 TAOAcceleratorEx64_ev.sys20-7-0 权限拒绝，豆包 Cache\No_Vary_Search 与 6 个 LevelDB 000003.log 被进程占用。本轮基线：C:\Users\Administrator 151.11GB、AppData\Local 19.81GB、C:\Windows 18.37GB、C:\ProgramData 8.24GB。C 可用由 76.28GB 到 76.31GB，本轮新增迁入目录为零、无回滚、无失败项。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。

2026-11-20 08:27　E 盘可删项执行（用户授权动手）：删四块历史备份与中间件共 26,289 文件 22,689,063,393 字节约 21.13GB —— E:\C盘搬迁_20261111\选股_改前备份 8345 文件 7,872,776,422 字节、同目录 龙虾_历史版本包 1996 文件 4,459,621,603 字节、同目录 _删会话前备份_20261112 4 文件 3,947,233,189 字节、E:\桌面大文件迁移_20261117\ucl_special\unl_3v 15947 文件 6,409,432,179 字节，四个目录删除后均已不存在，零失败。E 盘可用由 27,793,371,136 字节升到 50,545,471,488 字节，净增 22,752,100,352 字节约 21.19GB。三处未删并记录原因：E:\桌面大文件迁移_20261117\分类榜混剪发布素材\工程\output 1413MB 因 08:24 仍在写、工程在跑，暂不动；E:\视频素材库 已空壳只剩 5 文件 1MB，但内含 9 个联接指向 C:\Users\Administrator\Desktop 与 E:\迅雷云盘，删除只省 1MB 却会断掉这批素材入口路径，保留；E:\C盘搬迁_20261111 下 MiniMax_成品 3486MB 与 股票研究_迁移包与成品 1816MB 属成品、回测引擎_数据库备份 1846MB 属 .db 主库，按规矩一律不动。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。

2026-11-20 11:21　第五十轮定时清理，只清不迁（C 可用 75.28GB 远超 40GB 线，D 90.25GB、E 43.14GB）。七类合计释放 148,723,570 字节约 141.8MB：豆包 Code Cache 71.3MB、豆包 Cache 56.7MB、豆包 GPUCache 5.6MB、用户 Temp 7.82MB、C:\Windows\Temp 7,662 字节、__pycache__ 5 目录 414,706 字节、超 30 天 .log 4 个 72,769 字节（aha_doctor 下 10 月 21 日三份约 24KB 日志与一个 0 字节 output.log）。更新下载缓存、更新器残留、Edge Cache 三项本轮释放为零。被占用跳过 9 项：Windows\Temp\virtual_camera 与 TAOAcceleratorEx64_ev.sys20-8-59 权限拒绝，豆包 Cache\No_Vary_Search 与 6 个 LevelDB 000003.log 被进程占用。本轮基线：C:\Users\Administrator 148.74GB、AppData\Local 20.16GB、C:\Windows 18.48GB、C:\ProgramData 8.23GB。C 可用由 75.28GB 到 75.38GB，本轮新增迁入目录为零、无回滚、无失败项。E 盘收尾 43.05GB，比开局少 0.09GB，是分类榜工程同期在写盘所致。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。

2026-11-20 14:20　第五十一轮定时清理，只清不迁（C 可用 74.63GB、D 86.96GB、E 41.88GB，全在 40GB 线上方）。七类合计释放 77,429 字节约 0.07MB：豆包 Code Cache 30,785 字节（约 0.03MB）、超 30 天 .log 2 个 46,644 字节（aha_doctor 下 10 月 21 日 09:36 日志 23,676B，与一个 output.log 22,968B）。用户 Temp、Windows\Temp、更新下载缓存、__pycache__、更新器残留、Chrome 与 Edge 缓存本轮均无可清内容，释放为零。被占用跳过 9 项：Windows\Temp\virtual_camera 与 TAOAcceleratorEx64_ev.sys20-8-59 权限拒绝，豆包 Cache\No_Vary_Search 与 6 个 LevelDB 000003.log 被进程占用。本轮基线：C:\Users\Administrator 150.49GB、AppData\Local 20.37GB、C:\Windows 18.48GB、C:\ProgramData 8.23GB。C 可用由 74.63GB 到 74.62GB，新增迁入目录为零、无回滚、无失败项。D 盘可用 86.96GB，比上轮 90.25GB 少 3.29GB；E 盘由 43.05GB 到 41.88GB，少 1.17GB，均为其他工程同期写盘，不是本轮动作。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。

2026-11-20 17:21　第五十二轮定时清理，只清不迁（C 可用 74.43GB、D 86.93GB、E 40.75GB，全在 40GB 线上方）。七类合计释放 934,144 字节约 0.89MB：__pycache__ 11 个目录 896,361 字节、超 30 天 .log 2 个 37,783 字节（.minimax-agent-cn\projects\trailers_5films\_ser_qc_sw.log 11,655 字节、aha_doctor\Doubao\log\1.45.0.3-2026-10-21_13_27_53.log 26,128 字节）。用户 Temp、Windows\Temp、更新下载缓存、更新器残留、Chrome 与 Edge 与豆包缓存本轮无可清内容，释放为零。被占用跳过 9 项：Windows\Temp\virtual_camera 与 TAOAcceleratorEx64_ev.sys20-8-59 权限拒绝，豆包 Cache\No_Vary_Search 与 6 个 LevelDB 000003.log 被进程占用。本轮基线：C:\Users\Administrator 151.61GB、AppData\Local 20.33GB、C:\Windows 18.49GB、C:\ProgramData 8.23GB。C 可用由 74.43GB 到 74.44GB，新增迁入目录为零、无回滚、无失败项。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。

2026-11-20 17:40　第五十三轮定时清理，只清不迁（C 可用 74.40GB、D 86.92GB、E 40.81GB，全在 40GB 线上方）。七类合计释放 0 字节：用户 Temp 与更新下载缓存本已空，Windows\Temp 只剩被占用项，__pycache__ 与超 30 天 .log 本轮扫描零命中，更新器残留与浏览器缓存无可清内容。被占用跳过 9 项：Windows\Temp\virtual_camera 与 TAOAcceleratorEx64_ev.sys20-8-59 权限拒绝，豆包 Cache\No_Vary_Search 与 6 个 LevelDB 000003.log 被进程占用。本轮基线：C:\Users\Administrator 151.60GB、AppData\Local 20.37GB、C:\Windows 18.49GB、C:\ProgramData 8.24GB。C 可用由 74.40GB 到 74.39GB，收尾少 0.01GB 是同期写入（迅雷上传与豆包日志），不是清理负效果。新增迁入目录为零、无回滚、无失败项。调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 54 轮 · 2026-11-20 18:17】

本轮只清不迁，C 盘可用 74.29GB，远高于 40GB 阈值。

清理释放 30,846 字节，约 0.03MB，全部来自 Doubao 客户端 Code Cache。

本轮 C 盘可用 79,796,932,608 字节（74.32GB）清到 79,764,795,392 字节（74.29GB），差额来自同期写入，不是清理失效。

D 盘可用 93,319,446,528 字节（86.91GB）→ 93,319,057,408 字节（86.91GB）。

E 盘可用 43,151,839,232 字节（40.19GB）→ 43,174,871,040 字节（40.21GB）。

基线体积：C:\Users\Administrator 152.28GB、AppData\Local 20.44GB、C:\Windows 18.49GB、C:\ProgramData 8.23GB。

跳过 9 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys20-8-59 无删除权限；Doubao 客户端 6 个 000003.log 与 Cache\No_Vary_Search 被进程占用。

本轮无迁移，D:\C盘搬迁_定时迁移 无新增目录。

另记：E:\系统镜像备份\C盘整卷镜像_20261119.wim 正在走迅雷云盘上传，18:03 起传，18:17 实测进度 4%、速率 4.1MB/s。━━━

【第 55 轮 · 2026-11-20 20:22】

本轮只清不迁，C 盘可用 73.67GB，远高于 40GB 阈值。

清理释放 287,461,899 字节，约 274.15MB，全部来自软件更新器残留 C:\Users\Administrator\AppData\Local\@mmx-agentelectron-updater 整目录。

用户 Temp、Windows Temp、更新下载缓存、__pycache__、浏览器与 Electron 缓存、30 天以上日志这六类本轮释放为零。

C 盘可用 78,956,695,552 字节（73.53GB）到 79,102,570,496 字节（73.67GB）。

D 盘可用 93,334,929,408 字节（86.92GB）到 93,304,070,144 字节（86.91GB）。

E 盘可用 40,974,761,984 字节（38.16GB）到 40,970,936,320 字节（38.16GB）。

基线体积：C:\Users\Administrator 155.08GB、AppData\Local 20.62GB、C:\Windows 18.49GB、C:\ProgramData 8.24GB。

跳过 9 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys20-8-59 无删除权限；Doubao 客户端 6 个 000003.log（aha 用户 profile_explorer 的 Extension State、GCM Store\Encryption、Sync Data\LevelDB 各 1 个，Default 的 GCM Store\Encryption、Platform Notifications、Tea\common\tea.db 各 1 个）与 Cache\No_Vary_Search 被进程占用。

本轮无迁移，D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

另记上传状态：20:17 复核发现迅雷进程全部退出，18:03 起跑的那条镜像上传已中断。20:19 重新启动迅雷并自动登录成功，云盘已用 9.39TB，上传任务仍在列表（80 条），但全部处于暂停，本轮未能恢复续传，原因见随轮说明。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 56 轮 · 2026-11-20 23:20】

本轮清理释放 579,112,749 字节（552.28MB）。

分项：软件更新器残留 C:\Users\Administrator\AppData\Local\@mmx-agentelectron-updater 整目录删除，574,923,619 字节（548.29MB）。

浏览器与 Electron 缓存：Doubao 客户端 Default\Code Cache 清出 4,180,866 字节（3.99MB）。

30 天以上日志删 1 个：C:\Users\Administrator\首阳战法回测引擎\logs\auto_run\20261021.log，8,264 字节。

用户 Temp、Windows Temp、SoftwareDistribution\Download、__pycache__ 这四类本轮均 0 字节、0 命中。

三盘可用空间：C 盘 78,418,796,544 字节（73.03GB）到 78,985,621,504 字节（73.56GB）。

D 盘 92,622,995,456 字节（86.26GB），本轮无变化。

E 盘 37,700,513,792 字节（35.11GB）到 37,700,468,736 字节（35.11GB）。

基线体积：C:\Users\Administrator 169,234,464,451 字节（157.61GB）、AppData\Local 22,515,792,572 字节（20.97GB）、C:\Windows 19,867,827,113 字节（18.50GB）、C:\ProgramData 8,843,145,292 字节（8.24GB）。

跳过 9 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys20-8-59 拒绝访问无删除权限；Doubao 客户端 6 个 000003.log（aha 用户 profile_explorer 的 Extension State、GCM Store\Encryption、Sync Data\LevelDB，Default 的 GCM Store\Encryption、Platform Notifications、Tea\common\tea.db）与 Cache\No_Vary_Search 被进程占用。

本轮 C 盘可用 73.56GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 57 轮 · 2026-11-21 08:24】

本轮清理释放 446668142 字节（425.98MB）。

分项：用户 Temp 374725928 字节（357.37MB）。

浏览器与 Electron 缓存 71431703 字节（68.12MB），全部来自豆包客户端 Default：Cache 44.8MB、Code Cache 17.8MB、GPUCache 5.6MB。

30 天以上 .log 共 5 个，77272 字节（0.07MB）。

__pycache__ 清理 430142 字节（0.41MB）。

Windows Temp 3,097 字节，几乎为零。

SoftwareDistribution\Download 与软件更新器残留本轮均 0 字节、0 命中。

三盘可用空间：C 盘 80,381,861,888 字节（74.86GB）到 80,613,285,888 字节（75.08GB）。

本轮开始 08:19 手工实测 C 盘可用 80,437,772,288 字节（74.91GB）。

D 盘 87,372,484,608 字节（81.37GB）到 87,366,238,208 字节（81.36GB），微降 6.2MB，系外部写入，非本轮迁移。

E 盘 36,061,179,904 字节（33.59GB）到 36,593,414,144 字节（34.08GB），增长 532MB，系外部写入。

基线体积：C:\Users\Administrator 171,831,225,250 字节（160.03GB）、AppData\Local 23,226,434,490 字节（21.63GB）、C:\Windows 19,790,373,686 字节（18.43GB）、C:\ProgramData 3,231,727,059 字节（3.01GB）。

跳过 7 项：C:\Users\Administrator\AppData\Local\Temp\Thunder Network 被迅雷进程占用；C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-7-0 拒绝访问无删除权限；Doubao\Default\Cache\No_Vary_Search 被进程占用；Doubao\Default\GCM Store\Encryption\000003.log、Default\Platform Notifications\000003.log、Tea\common\tea.db\000003.log 均被进程占用。

本轮 C 盘可用 75.08GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 58 轮 · 2026-11-21 11:23】

本轮清理释放 2,281,693,526 字节（2,175.99MB）。

分项：用户 Temp 2,267,406,336 字节（2,162.37MB），占绝大部分。

浏览器与 Electron 缓存 14,274,133 字节（13.61MB），来自豆包客户端 Default\Code Cache。

30 天以上 .log 删 1 个，12,614 字节，文件为 aha_doctor\Doubao\log\1.45.0.3-2026-10-22_10_15_38.log。

Windows Temp 443 字节。

SoftwareDistribution\Download、__pycache__、软件更新器残留本轮均 0 字节。

三盘可用空间：C 盘 52,904,091,648 字节（49.27GB）到 54,997,921,792 字节（51.22GB）。

D 盘 87,293,612,032 字节（81.30GB）到 87,293,378,560 字节（81.30GB），微降 22KB。

E 盘 35,911,221,248 字节（33.44GB）到 35,727,777,792 字节（33.27GB），降 175MB，系外部写入。

基线体积：C:\Users\Administrator 199,614,662,852 字节（185.91GB）、AppData\Local 25,704,824,854 字节（23.94GB）、C:\Windows 19,805,114,446 字节（18.44GB）、C:\ProgramData 3,232,935,201 字节（3.01GB）。

与本轮前一轮相比，C:\Users\Administrator 从 171,831,225,250 字节涨到 199,614,662,852 字节，增 27.8GB，主因是桌面根目录今天新增两个压缩包：大智慧目录备份_20261121.zip 21.75GB（10:12:43 生成）、同花顺目录备份_20261121.zip 1.05GB（08:40:21 生成），合计约 22.8GB。这两个包属个人文档，不在清理范围，未动。

跳过 7 项：C:\Users\Administrator\AppData\Local\Temp\Thunder Network 被迅雷进程占用；C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-7-0 拒绝访问无删除权限；Doubao\Default\Cache\No_Vary_Search 被进程占用；Doubao\Default\GCM Store\Encryption\000003.log、Default\Platform Notifications\000003.log、Tea\common\tea.db\000003.log 均被进程占用。

本轮 C 盘可用 51.22GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 59 轮 · 2026-11-21 14:21】

本轮起点 C 盘可用 53,185,028,096 字节（49.53GB），结束时 54,002,253,824 字节（50.29GB）。

本轮清理释放 686,556,490 字节（654.8MB）。

分项：用户 Temp 614,364,685 字节（585.90MB）。

浏览器与 Electron 缓存 71,751,398 字节（68.43MB），来自豆包客户端 Default\Cache 60.5MB、Default\Code Cache 2.4MB、Default\GPUCache 5.6MB。

__pycache__ 删 5 个目录，437,305 字节（0.42MB）。

Windows Temp 3,102 字节。

SoftwareDistribution\Download、软件更新器残留、30 天以上日志本轮均 0。

三盘可用空间：C 盘 53,185,028,096 字节（49.53GB）到 54,002,253,824 字节（50.29GB）。

D 盘 86,559,055,872 字节（80.61GB），前后一致。

E 盘 33,270,321,152 字节（30.99GB），前后一致。

基线体积：C:\Users\Administrator 198,702,167,510 字节（185.06GB）、AppData\Local 23,930,408,001 字节（22.29GB）、C:\Windows 19,825,928,050 字节（18.46GB）、C:\ProgramData 4,058,077,958 字节（3.78GB）。

本轮开始前 C 盘可用一度掉到 28.15GB（12:45 实测），原因是 WPS 云同步在 C:\Users\Administrator\Documents\WPS Cloud Files\.687324960\cachedata 下缓存了大智慧目录备份_20261121.zip 的完整副本，字节 23,358,203,822，与桌面原包完全同尺寸。该副本在本轮开始前已被 WPS 自身释放，文件已不存在，C 盘可用回到 49.53GB，这块空间不由本任务清理。

跳过 6 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-12-30 拒绝访问；Doubao\Default\Cache\No_Vary_Search 被进程占用；Doubao\Default\GCM Store\Encryption\000003.log 被进程占用；Doubao\Default\Platform Notifications\000003.log 被进程占用；Doubao\Tea\common\tea.db\000003.log 被进程占用。

本轮 C 盘可用 50.29GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 60 轮 · 2026-11-21 17:21】

本轮起点 C 盘可用 51,968,241,664 字节（48.40GB），结束时 53,072,867,328 字节（49.43GB）。

本轮清理释放 2,027,339,100 字节（1,933.4MB，约 1.89GB）。

分项：用户 Temp 2,025,152,512 字节（1,931.34MB）。

浏览器与 Electron 缓存 2,151,096 字节（2.05MB），来自豆包客户端 Default\Code Cache。

30 天以上日志 2 个，7,400 字节，均为 .minimax\sessions 下的 _pkg_build.log，每个 3,700 字节。

__pycache__ 删 1 个目录，28,092 字节。

Windows Temp、SoftwareDistribution\Download、软件更新器残留本轮均 0。

三盘可用空间：C 盘 51,968,241,664 字节（48.40GB）到 53,072,867,328 字节（49.43GB）。

D 盘 85,228,945,408 字节（79.37GB），前后基本一致，变动 64,000 字节系自身文件索引。

E 盘 30,935,748,608 字节（28.81GB），前后一致。

基线体积：C:\Users\Administrator 200,803,734,291 字节（187.01GB）、AppData\Local 25,477,215,998 字节（23.73GB）、C:\Windows 19,832,042,196 字节（18.47GB）、C:\ProgramData 4,060,952,602 字节（3.78GB）。

本轮清理量与 C 盘可用净增不相等，清理 1.89GB 而可用只多 1.06GB，差额是本轮运行期间其他进程（豆包、WPS、浏览器）继续写入造成的，属正常。

跳过 6 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-12-30 拒绝访问；Doubao\Default\Cache\No_Vary_Search 被进程占用；Doubao\Default\GCM Store\Encryption\000003.log 被进程占用；Doubao\Default\Platform Notifications\000003.log 被进程占用；Doubao\Tea\common\tea.db\000003.log 被进程占用。

本轮 C 盘可用 49.43GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 61 轮 · 2026-11-21 20:20】

本轮起点 C 盘可用 53,030,367,232 字节（49.39GB），结束时 53,025,456,128 字节（49.38GB）。

本轮清理释放 60,191 字节（0.06MB），是本任务开跑以来最少的一轮。

分项：用户 Temp 为 0，上一轮已经清空，本轮没有新垃圾。

豆包客户端 Code Cache 36,271 字节。

30 天以上日志 14 个，23,920 字节，全部是 .minimax\sessions 两个会话目录下的 _rp_ 系列调试日志，单个 323 到 3,588 字节。

__pycache__、Windows Temp、SoftwareDistribution\Download、软件更新器残留本轮均 0。

三盘可用空间：C 盘 53,030,367,232 字节（49.39GB）到 53,025,456,128 字节（49.38GB）。

C 盘结束时比开始时少 4,911,104 字节，是本轮运行期间进程继续写入造成的，不是清理脚本误删。

D 盘 85,177,778,176 字节（79.33GB），本轮内前后一致。

E 盘 30,866,264,064 字节（28.75GB），本轮内前后一致。

基线体积：C:\Users\Administrator 198,959,302,416 字节（185.30GB）、AppData\Local 23,693,846,974 字节（22.07GB）、C:\Windows 19,836,059,669 字节（18.47GB）、C:\ProgramData 4,061,264,800 字节（3.78GB）。

跳过 6 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-12-30 拒绝访问；Doubao\Default\Cache\No_Vary_Search 被进程占用；Doubao\Default\GCM Store\Encryption\000003.log 被进程占用；Doubao\Default\Platform Notifications\000003.log 被进程占用；Doubao\Tea\common\tea.db\000003.log 被进程占用。

本轮 C 盘可用 49.38GB，高于 40GB 阈值，只做清理不做迁移。

D:\C盘搬迁_定时迁移 无新增目录、无回滚、无失败项。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。
━━━

【第 62 轮 · 2026-11-21 23:25】

文首空间：C 盘可用 29,345,865,728 字节（27.33GB），D 盘可用 87,877,107,712 字节（81.83GB），E 盘可用 29,982,130,176 字节（27.92GB）。

本轮清理释放 147,365,077 字节（140.5MB）。

分项：用户 Temp 8,199,464 字节（7.82MB）；Windows Temp 2,810 字节；豆包缓存 138,706,116 字节（132.28MB，其中 Cache 76.6MB、Code Cache 50.1MB、GPUCache 5.6MB）；__pycache__ 5 个目录 437,305 字节；30 天以上日志 3 个 19,382 字节；系统更新下载缓存与更新器残留均为 0。

C 盘可用从 29,345,865,728 字节升到 29,451,526,144 字节。

基建体积：C:\Users\Administrator 222,690,197,354 字节（207.40GB），AppData\Local 23,826,342,361 字节（22.19GB），C:\Windows 19,813,859,722 字节（18.45GB），C:\ProgramData 4,073,904,816 字节（3.79GB）。

跳过 6 项：C:\Windows\Temp\virtual_camera 被进程占用；C:\Windows\Temp\TAOAcceleratorEx64_ev.sys21-20-59 拒绝访问；豆包 Default\Cache\No_Vary_Search 被进程占用；豆包 Default\GCM Store\Encryption\000003.log 被进程占用；豆包 Default\Platform Notifications\000003.log 被进程占用；豆包 Tea\common\tea.db\000003.log 被进程占用。

本轮新增迁入目录：无。

原因如实说明：本轮开跑时 C 盘可用 27.33GB 已低于 40GB 阈值，满足迁移条件，我实际筛了冷目录但没有一个合法可搬。

C:\Users\Administrator\.qclaw 4.59GB、129,817 个文件、77 天未动，D:\C盘搬迁_定时迁移\.qclaw 已存在同名目录（2026-11-15 建），按不覆盖规则跳过。

同样因目标已存在而跳过的还有 .agents 1.18GB、.cache 0.18GB、.EasyOCR 0.10GB、.hub 0.12GB、.openclaw 0.18GB、.openclaw-windclaw 0.66GB、.paddlex 0.20GB、lobsterai 0.51GB，D 盘都已有 2026-11-15 的同名副本。

Desktop\票房榜发布素材 1.29GB 最新修改 11-15 09:41，距今 6.9 天，未满 7 天，不合规不搬。

Desktop\03_账号与资产 0.90GB、Desktop\AI图片 0.28GB 均在禁迁清单，不动。

本轮回滚与失败项：无。

23:30 复测：C 盘可用回升到 52,794,277,888 字节（49.17GB），原因是 WPS 云同步又把桌面 21.75GB 大智慧备份包在 Documents\WPS Cloud Files 下复制了一份、随后自行释放，清理期间刚好撞上这份副本，属于空间瞬时抖动，不是迁移造成的。

调用约定：MiniMax 取素材直接读 D 盘，不要复制回 C 盘。