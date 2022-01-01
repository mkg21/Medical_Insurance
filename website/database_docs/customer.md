###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>customer


# ![logo](../../../../../Images/table64.svg) customer

## <a name="#Description"></a>Description
> The customer of the medical insurance company.> 
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|id|INT||11||False|False|False|True|True||False|The id of the customer|
||f_name|VARCHAR|20|||False|False|False|True|False||False|The first name of the customer|
||m_name|VARCHAR|20|||False|False|False|True|False||False|The middle name of the customer|
||l_name|VARCHAR|20|||False|False|False|True|False||False|The last name of the customer|
||e_mail|VARCHAR|30|||False|False|False|True|False||False|The email address of the customer|
||address|VARCHAR|50|||False|False|False|True|False||False|The address of the customer|
||b_date|DATE|0|||False|False|False|True|False||False|The birth date of the customer|
||gender|VARCHAR|6|||False|False|False|True|False||False|The gender of the customer|
||phone|CHAR|11|||False|False|False|True|False||False|The phone number of the customer|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE customer (
  id INT NOT NULL AUTO_INCREMENT,
  f_name VARCHAR(20) NOT NULL,
  m_name VARCHAR(20) NOT NULL,
  l_name VARCHAR(20) NOT NULL,
  e_mail VARCHAR(30) NOT NULL,
  address VARCHAR(50) NOT NULL,
  b_date DATE NOT NULL,
  gender VARCHAR(6) NOT NULL,
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
- ![Table](../../../../../Images/table.svg) [contract](contract.md)
- ![Table](../../../../../Images/table.svg) [dependent](dependent.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial