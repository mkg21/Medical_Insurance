###### Medical Insurance Company
___
[Project](../../../../../startpage.md)>[Servers](../../../../Servers.md)>[localhost](../../../localhost.md)>[Databases](../../Databases.md)>[medical_insurance](../medical_insurance.md)>[Tables](Tables.md)>contract


# ![logo](../../../../../Images/table64.svg) contract

## <a name="#Description"></a>Description
> The contract between the customer or any of his/her dependents and the medical insurance company.
## <a name="#Columns"></a>Columns
|Key|Name|Data Type|Length|Precision|Scale|Unsigned|Zerofill|Binary|Not Null|Auto Increment|Default|Virtual|Description|
|:---:|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[![Primary Key ](../../../../../Images/primarykey.svg)](#Indexes)|id|INT||11||False|False|False|True|True||False|Contract id|
|[![Foreign Keys contract_ibfk_3: plan](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes plan_id](../../../../../Images/index.svg)](#Indexes)|plan_id|INT||11||False|False|False|True|False||False|Id of the plan purchased regarding to this contract|
|[![Foreign Keys contract_ibfk_1: customer](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes cus_id](../../../../../Images/index.svg)](#Indexes)|cus_id|INT||11||False|False|False|False|False|NULL|False|The id of the customer beneficiary of this plan.|
|[![Foreign Keys contract_ibfk_2: dependent](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes res_id](../../../../../Images/index.svg)](#Indexes)|res_id|INT||11||False|False|False|False|False|NULL|False|The id of the customer responsible of the beneficiary dependent of this plan|
|[![Foreign Keys contract_ibfk_2: dependent](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes res_id](../../../../../Images/index.svg)](#Indexes)|dep_name|VARCHAR|20|||False|False|False|False|False|NULL|False|The name of the beneficiary dependent of this plan|
|[![Foreign Keys contract_ibfk_2: dependent](../../../../../Images/foreignkey.svg)](#ForeignKeys)[![Indexes res_id](../../../../../Images/index.svg)](#Indexes)|kinship|VARCHAR|20|||False|False|False|False|False|NULL|False|The kinship between the beneficiary dependent of this plan and his/her responsible customer |
||payment_method|VARCHAR|20|||False|False|False|False|False|NULL|False|The payment details used to buy this plan.|

## <a name="#Indexes"></a>Indexes
|Key|Name|Columns|Unique|Type|Key Lengths|
|:---:|---|---|---|---|---|
||cus_id|cus_id|True|None||
||res_id|res_id, dep_name, kinship|True|None||
||plan_id|plan_id|False|None||

## <a name="#CheckConstraints"></a>Check Constraints
|Name|Columns|Check Constraints|
|---|---|---|
|contract_chk_1|cus_id, res_id, dep_name, kinship|(((`cus_id` is not null) or ((`res_id` is not null) and (`dep_name` is not null) and (`kinship` is not null))))|
|contract_chk_2|cus_id, res_id|((((`cus_id` is null) and (`res_id` is not null)) or ((`cus_id` is not null) and (`res_id` is null))))|

## <a name="#ForeignKeys"></a>Foreign Keys
|Name|Columns|Delete Rule|Update Rule|
|---|---|---|---|
|contract_ibfk_1|id|N/S|N/S|
|contract_ibfk_2|cus_id, name, kinship|N/S|N/S|
|contract_ibfk_3|id|N/S|N/S|

## <a name="#SqlScript"></a>SQL Script
```SQL
CREATE TABLE contract (
  id INT NOT NULL AUTO_INCREMENT,
  plan_id INT NOT NULL,
  cus_id INT DEFAULT NULL,
  res_id INT DEFAULT NULL,
  dep_name VARCHAR(20) DEFAULT NULL,
  kinship VARCHAR(20) DEFAULT NULL,
  payment_method VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

ALTER TABLE contract 
  ADD CONSTRAINT contract_chk_1 CHECK ((`cus_id` is not null) or ((`res_id` is not null) and (`dep_name` is not null) and (`kinship` is not null)));

ALTER TABLE contract 
  ADD CONSTRAINT contract_chk_2 CHECK (((`cus_id` is null) and (`res_id` is not null)) or ((`cus_id` is not null) and (`res_id` is null)));

ALTER TABLE contract 
  ADD UNIQUE INDEX cus_id(cus_id);

ALTER TABLE contract 
  ADD UNIQUE INDEX res_id(res_id, dep_name, kinship);

ALTER TABLE contract 
  ADD CONSTRAINT contract_ibfk_1 FOREIGN KEY (cus_id)
    REFERENCES customer(id);

ALTER TABLE contract 
  ADD CONSTRAINT contract_ibfk_2 FOREIGN KEY (res_id, dep_name, kinship)
    REFERENCES dependent(cus_id, name, kinship);

ALTER TABLE contract 
  ADD CONSTRAINT contract_ibfk_3 FOREIGN KEY (plan_id)
    REFERENCES plan(id);
```

## <a name="#DependsOn"></a>Depends On _`3`_
- ![Table](../../../../../Images/table.svg) [customer](customer.md)
- ![Table](../../../../../Images/table.svg) [dependent](dependent.md)
- ![Table](../../../../../Images/table.svg) [plan](plan.md)


## <a name="#UsedBy"></a>Used By _`1`_
- ![Table](../../../../../Images/table.svg) [claim](claim.md)


||||
|---|---|---|
|Author: Database Team||Created: 1/1/2022|
# dbForge Documenter Trial