###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>dependent


# ![logo](../../../../../Images/table64.svg) dependent

## <a name="#Description"></a>Description
> the dependent of a certain customer.
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)[![Foreign Keys dependent_ibfk_1: customer](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes `cus_id`](../../../../../Images/index.svg)](#Indexes)|cus_id|INT||11||False|False|False|True|False||False|The id of the customer who is responsible of the dependent|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|name|VARCHAR|20|||False|False|False|True|False||False|The first name of the dependent|
||b_date|DATE|0|||False|False|False|True|False||False|the birth date of the dependent|
||gender|VARCHAR|6|||False|False|False|True|False||False|The gender of the dependent|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|kinship|VARCHAR|20|||False|False|False|True|False||False|The kinship between the dependent and his/her responsible customer |

## <a name="#Indexes"></a>Indexes
|Key|Name|Columns|Unique|Type|Key Lengths|
|:---:|---|---|---|---|---|
||`cus_id`|cus_id|False|None||

## <a name="#ForeignKeys"></a>Foreign Keys
|Name|Columns|Delete Rule|Update Rule|
|---|---|---|---|
|dependent_ibfk_1|id|N/S|N/S|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE dependent (
  cus_id INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  b_date DATE NOT NULL,
  gender VARCHAR(6) NOT NULL,
  kinship VARCHAR(20) NOT NULL,
  PRIMARY KEY (cus_id, name, kinship)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE dependent 
  ADD CONSTRAINT dependent_ibfk_1 FOREIGN KEY (cus_id)
    REFERENCES customer(id);
```

## <a name="#DependsOn"></a>Depends On _`1`_
- ![Table](../../../../../Images/table.svg) [customer](customer.md)


## <a name="#UsedBy"></a>Used By _`1`_
- ![Table](../../../../../Images/table.svg) [contract](contract.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial