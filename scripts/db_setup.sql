CREATE DATABASE queue_simulation;

CREATE TABLE `customers` (
	`id` INT(1) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT COMMENT 'Primary key',
	`biometric` VARCHAR(36) NULL DEFAULT NULL COMMENT 'Contains biometric data',
	`customer_status` ENUM('NORMAL','REGULAR','VIP') NULL DEFAULT NULL COMMENT 'Describes the customer judging the frequency',
	`is_new` SMALLINT(1) NULL DEFAULT NULL COMMENT 'Informs if the customer was known before the simulation started running',
	PRIMARY KEY (`id`),
	UNIQUE INDEX `biometric` (`biometric`)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=128;
