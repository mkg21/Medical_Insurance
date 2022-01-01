###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>enrolled


# ![logo](../../../../../Images/table64.svg) enrolled

## <a name="#Description"></a>Description
> The relationship between hospitals and the plans covered by each hospital.
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Foreign Keys enrolled_ibfk_1: hospital](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes no_dup](../../../../../Images/index.svg)](#Indexes)|hos_id|INT||11||False|False|False|True|False||False|The id of the hospital|
|[![Foreign Keys enrolled_ibfk_2: plan](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes no_dupplan_id](../../../../../Images/index.svg)](#Indexes)|plan_id|INT||11||False|False|False|True|False||False|The id of the plan|

## <a name="#Indexes"></a>Indexes
|Key|Name|Columns|Unique|Type|Key Lengths|
|:---:|---|---|---|---|---|
||no_dup|hos_id, plan_id|True|None||
||plan_id|plan_id|False|None||

## <a name="#ForeignKeys"></a>Foreign Keys
|Name|Columns|Delete Rule|Update Rule|
|---|---|---|---|
|enrolled_ibfk_1|id|N/S|N/S|
|enrolled_ibfk_2|id|N/S|N/S|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE enrolled (
  hos_id INT NOT NULL,
  plan_id INT NOT NULL
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE enrolled 
  ADD UNIQUE INDEX no_dup(hos_id, plan_id);

ALTER TABLE enrolled 
  ADD CONSTRAINT enrolled_ibfk_1 FOREIGN KEY (hos_id)
    REFERENCES hospital(id);

ALTER TABLE enrolled 
  ADD CONSTRAINT enrolled_ibfk_2 FOREIGN KEY (plan_id)
    REFERENCES plan(id);
```

## <a name="#DependsOn"></a>Depends On _`2`_
- ![Table](../../../../../Images/table.svg) [hospital](hospital.md)
- ![Table](../../../../../Images/table.svg) [plan](plan.md)


## <a name="#UsedBy"></a>Used By
No items found

||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial