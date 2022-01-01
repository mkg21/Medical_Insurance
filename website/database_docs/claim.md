###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>claim


# ![logo](../../../../../Images/table64.svg) claim

## <a name="#Description"></a>Description
> Claim entity describes the claim insurance filed by the customer and can be reviewed by the admin to get accepted or rejected.> 
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|id|INT||11||False|False|False|True|True||False|The Id of the claim|
|[![Foreign Keys claim_ibfk_1: contract](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes con_id](../../../../../Images/index.svg)](#Indexes)|con_id|INT||11||False|False|False|True|False||False|The id of the contract that this claim is filed under|
|[![Foreign Keys claim_ibfk_2: hospital](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes hos_id](../../../../../Images/index.svg)](#Indexes)|hos_id|INT||11||False|False|False|True|False||False|The id of the hospital linked to this claim|
||expenses|DECIMAL||10|2|False|False|False|True|False||False|The amount of expanses of this claim in Egyptian Pounds.|
||expenses_subject|TEXT||||False|False|False|True|False||False|The subject of the claim|
||expenses_details|TEXT||||False|False|False|True|False||False|The details about the expenses regarding to this claim.|
||status|TINYINT||4||False|False|False|False|False|NULL|False|The status of the claim which can be:
null (default value): the claim file is yet to be resolved
0: the claim file is denied
1: the claim file is accepted|
||date|DATE|0|||False|False|False|True|False||False|The date this claim is filed in.|

## <a name="#Indexes"></a>Indexes
|Key|Name|Columns|Unique|Type|Key Lengths|
|:---:|---|---|---|---|---|
||con_id|con_id|False|None||
||hos_id|hos_id|False|None||

## <a name="#ForeignKeys"></a>Foreign Keys
|Name|Columns|Delete Rule|Update Rule|
|---|---|---|---|
|claim_ibfk_1|id|N/S|N/S|
|claim_ibfk_2|id|N/S|N/S|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE claim (
  id INT NOT NULL AUTO_INCREMENT,
  con_id INT NOT NULL,
  hos_id INT NOT NULL,
  expenses DECIMAL(10, 2) NOT NULL,
  expenses_subject TEXT NOT NULL,
  expenses_details TEXT NOT NULL,
  status TINYINT DEFAULT NULL,
  date DATE NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE claim 
  ADD CONSTRAINT claim_ibfk_1 FOREIGN KEY (con_id)
    REFERENCES contract(id);

ALTER TABLE claim 
  ADD CONSTRAINT claim_ibfk_2 FOREIGN KEY (hos_id)
    REFERENCES hospital(id);
```

## <a name="#DependsOn"></a>Depends On _`2`_
- ![Table](../../../../../Images/table.svg) [contract](contract.md)
- ![Table](../../../../../Images/table.svg) [hospital](hospital.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial