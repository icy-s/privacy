import json

companyName=input("Sisestage oma ettevõtte nimi: ")

while True:
    contactEmail=input("Sisestage oma isiklik e-mail address: ")
    if "@" in contactEmail:
        break
    else:
        print("где собака")

dataCollectionType=input("Millised andmed salvestame: ")
dataUsage=input("Kuidas andmed kasutatakse: ")
dataStorageLimit=input("Kui kaua andmed salvestatakse: ")
cookieQuestion=input("Kas oled nõus cookie-ga salvestamisega (jah/ei)? ")



privacyData = {
    "company_name":companyName,
    "contact_email":contactEmail,
    "data_collection_type":dataCollectionType,
    "data_usage":dataUsage,
    "data_storage_limit":dataStorageLimit,
    "cookie_agreement":cookieQuestion
    }

with open("privacy_template.json","w",encoding="utf-8") as file:
    json.dump(privacyData, file, indent = 4)
print("molodec")

html_template ="""
<!DOCTYPE html>
<html>	
<head>
<title> Privaatsuspoliitika </title>
<head>
<body>
    <h1>Poliitika pühendanud ettevõttele - {company_name} </h1>
    <p>Kontakt: {contact_email}</p>
    <h2>Millised andmed kogume?</h2>
    <p>{data_collection_type}</p>
    <h2>Kuidas andmed kasutatakse</h2>
    <p>{data_usage}</p>
    <h2>Kui kaua salvestame?</h2>
    <p>{data_storage_limit}</p>
    <h2>Kas oled nõus cookie-ga salvestamisega? (jah/ei)</h2>
    <p>{cookie_agreement}</p>

</body>
</html>
"""


privacy_policy= html_template.format(**privacyData)

with open("privacy_template.html","w",encoding="utf-8") as file:
    file.write(privacy_policy)
print("""
    >   ／＞　 フ
   | 　_　_| 
  ／` ミ＿xノ 
 /　　　　 |
 /　 ヽ　　 ﾉ
 │　　|　|　|
 ／￣|　　 |　
 (￣ヽ＿_ヽ_)
""")
    
    
    
    