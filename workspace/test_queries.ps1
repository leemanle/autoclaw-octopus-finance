$apiKey = "mkt_Ceuq_sbzJtsaKFRYC3K-NFkxX9jHeRA-J0MQKTSltuo"
$url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/query"

$queries = @(
    "贵州茅台股票",
    "上证指数",
    "A股今日行情",
    "今日涨停板",
    "东方财富股票"
)

foreach ($q in $queries) {
    Write-Host "`n=== 查询: $q ===" -ForegroundColor Cyan
    $body = @{
        toolQuery = $q
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -Header @{apikey=$apiKey} -TimeoutSec 30
        $data = $response.data.data.searchDataResultDTO
        if ($data.dataTableDTOList.Count -gt 0) {
            Write-Host "✓ 找到 $($data.dataTableDTOList.Count) 条数据" -ForegroundColor Green
            $data.dataTableDTOList | ForEach-Object {
                Write-Host "  - $($_.entityName): $($_.title)"
            }
        } else {
            Write-Host "✗ 无数据" -ForegroundColor Red
        }
    } catch {
        Write-Host "✗ 错误: $_" -ForegroundColor Red
    }
}
