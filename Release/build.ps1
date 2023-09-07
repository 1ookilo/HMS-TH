# $TimeZone = [System.TimeZoneInfo]::FindSystemTimeZoneById("SE Asia Standard Time")
# $Tag = [System.TimeZoneInfo]::ConvertTime($(Get-Item Release/HMS_00-WindowsNoEditor_P.pak).LastWriteTime, $TimeZone).ToString("ddMMyyyy")
# echo "MY_TAG=$Tag" | Out-File -FilePath $env:GITHUB_ENV -Append
# # $Path = "HMS_00"
# # New-Item -Name "$Path" -ItemType "directory" -Force
# # New-Item -Path "$Path" -Name "Content" -ItemType "directory" -Force
# # New-Item -Path "$Path/Content" -Name "Paks" -ItemType "directory" -Force
# # $Pak_Path = "$Path/Content/Paks"
# # Copy-Item -Path Release/HMS_00-WindowsNoEditor_P.pak $Pak_Path -Force
# # 7z a -t7z "./Release/HMS_TH_$Tag.7z" "HMS_00" -mx=9 -ms
# # Set-Location "../"


# $Path = "Release"
# New-Item -Name "$Path" -ItemType "directory" -Force
# New-Item -Path "$Path" -Name "HMS_00" -ItemType "directory" -Force
# New-Item -Path "$Path/HMS_00" -Name "Content" -ItemType "directory" -Force
# New-Item -Path "$Path/HMS_00/Content" -Name "Paks" -ItemType "directory" -Force
# $Pak_Path = "$Path/HMS_00/Content/Paks"
# Set-Location "$Path"
# Copy-Item -Path HMS_00-WindowsNoEditor_P.pak $Pak_Path -Force

# 7z a -t7z "./Release/HMS_TH_$Tag.7z" "HMS_00/" -mx=9 -ms
# Set-Location "../"

$TimeZone = [System.TimeZoneInfo]::FindSystemTimeZoneById("SE Asia Standard Time")
$Tag = [System.TimeZoneInfo]::ConvertTime($(Get-Item Release/HMS_00-WindowsNoEditor_P.pak).LastWriteTime, $TimeZone).ToString("ddMMyyyy")
echo "MY_TAG=$Tag" | Out-File -FilePath $env:GITHUB_ENV -Append
$Path = "Release/HMS_00/Content/Paks"  # แก้โค้ดเป็น path ที่ถูกต้อง
New-Item -Path $Path -ItemType "directory" -Force
Copy-Item -Path Release/HMS_00-WindowsNoEditor_P.pak -Destination $Path -Force
Set-Location "Release"

7z a -t7z "./HMS_TH_$Tag.7z" "HMS_00/" -mx=9 -ms
Set-Location "../"