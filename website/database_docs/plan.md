###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>plan


# ![logo](../../../../../Images/table64.svg) plan

## <a name="#Description"></a>Description
> The insurance plans offered by the company.
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|id|INT||11||False|False|False|True|True||False|The id of the plan|
|[![Indexes type](../../../../../Images/index.svg)](#Indexes)|type|VARCHAR|20|||False|False|False|True|False||False|The type (name) of the plan|
||benefits|TEXT||||False|False|False|True|False||False|The benefits offered by the plan|
||price|DECIMAL||8|2|False|False|False|True|False||False|The price of the plan in Egyptian pounds|

## <a name="#Indexes"></a>Indexes
|Key|Name|Columns|Unique|Type|Key Lengths|
|:---:|---|---|---|---|---|
||type|type|True|None||

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE plan (
  id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(20) NOT NULL,
  benefits TEXT NOT NULL,
  price DECIMAL(8, 2) NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE plan 
  ADD UNIQUE INDEX type(type);
```

## <a name="#DependsOn"></a>Depends On
No items found

## <a name="#UsedBy"></a>Used By _`2`_
- ![Table](../../../../../Images/table.svg) [contract](contract.md)
- ![Table](../../../../../Images/table.svg) [enrolled](enrolled.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial