$apiKey = "mkt_Ceuq_sbzJtsaKFRYC3K-NFkxX9jHeRA-J0MQKTSltuo"
$url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/query"

$queries = @("贵州茅台", "上证指数", "A股")

foreach ($q in $queries) {
    Write-Host "`n=== Query: $q ===" -ForegroundColor Cyan
    $body = @{toolQuery = $q} | ConvertTo-Json -Encoding UTF8
    $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json; charset=utf-8" -Header @{apikey=$apiKey} -TimeoutSec 30
    $data = $response.data.data.searchDataResultDTO
    Write-Host "Data count: $($data.dataTableDTOList.Count)"
    if ($data.dataTableDTOList.Count -gt 0) {
        $data.dataTableDTOList | Select-Object -First 3 | ForEach-Object {
            Write-Host "  - $($_.entityName)"
        }
    }
}
