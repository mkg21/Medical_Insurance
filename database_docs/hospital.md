###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>hospital


# ![logo](../../../../../Images/table64.svg) hospital

## <a name="#Description"></a>Description
> The hospitals contracted with the company.
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|id|INT||11||False|False|False|True|True||False|The id of the hospital|
||name|VARCHAR|20|||False|False|False|True|False||False|The name of the hospital|
||address|VARCHAR|50|||False|False|False|True|False||False|The Address of the hospital|
||e_mail|VARCHAR|30|||False|False|False|True|False||False|The official email address of the hospital|
||phone|CHAR|11|||False|False|False|True|False||False|The official telephone number of the hospital|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE hospital (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(20) NOT NULL,
  address VARCHAR(50) NOT NULL,
  e_mail VARCHAR(30) NOT NULL,
  phone CHAR(11) NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;
```

## <a name="#DependsOn"></a>Depends On
No items found

## <a name="#UsedBy"></a>Used By _`2`_
- ![Table](../../../../../Images/table.svg) [claim](claim.md)
- ![Table](../../../../../Images/table.svg) [enrolled](enrolled.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial