SELECT `employee
`.`name`,
    `employee`.`idc`,
    `employee`.`city`
FROM `Bolivar_insurer`.`employee`;

UPDATE `Bolivar_insurer`.`employee`
SET
`city` = 'Cali'
WHERE `id` = 7;