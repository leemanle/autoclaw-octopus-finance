$apiKey = "mkt_Ceuq_sbzJtsaKFRYC3K-NFkxX9jHeRA-J0MQKTSltuo"
$url = "https://mkapi2.dfcfs.com/finskillshub/api/claw/query"
$body = @{
    toolQuery = "茅台最新价"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -Header @{apikey=$apiKey}
$response | ConvertTo-Json -Depth 10
