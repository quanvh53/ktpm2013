SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `template_v2` DEFAULT CHARACTER SET utf8 ;
USE `template_v2` ;

-- -----------------------------------------------------
-- Table `template_v2`.`admin`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`admin` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `user` TEXT NOT NULL ,
  `fullname` TEXT NULL DEFAULT NULL ,
  `pass` TEXT NOT NULL ,
  `email` TEXT NOT NULL ,
  `nick` TEXT NULL DEFAULT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`an_uong`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`an_uong` (
  `ten_au` VARCHAR(45) NOT NULL ,
  `mieu_ta_au` TEXT NULL DEFAULT NULL ,
  `hinh_au` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`ten_au`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`banner`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`banner` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_banner` TEXT NOT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`feed_back`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`feed_back` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `tieu_de` TEXT NOT NULL ,
  `name` TEXT NOT NULL ,
  `phone` BIGINT(20) NULL DEFAULT NULL ,
  `email` TEXT NOT NULL ,
  `nhan_xet` TEXT NOT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`footer`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`footer` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_footer` TEXT NULL DEFAULT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `slogen` TEXT NULL DEFAULT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`gioi_thieu`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`gioi_thieu` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_1` TEXT NOT NULL ,
  `hinh_2` TEXT NULL DEFAULT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `noi_dung` TEXT NOT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`logo`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`logo` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_logo` TEXT NOT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `slogen` TEXT NULL DEFAULT NULL ,
  `date` DATE NULL DEFAULT NULL ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`menu`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`menu` (
  `idMenu` INT(11) NOT NULL AUTO_INCREMENT ,
  `nameMenu` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL ,
  `linkMenu` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL ,
  `newPageMenu` INT(11) NOT NULL DEFAULT '0' ,
  `isParent` INT(11) NOT NULL DEFAULT '1' ,
  `parentId` INT(11) NULL DEFAULT '0' ,
  `order` INT(11) NULL DEFAULT NULL ,
  `status` INT(11) NOT NULL DEFAULT '1' ,
  PRIMARY KEY (`idMenu`) )
ENGINE = MyISAM
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`quang_cao`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`quang_cao` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_qc` TEXT NOT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `noi_dung` TEXT NULL DEFAULT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`san_pham`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`san_pham` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `title_child_id` INT(11) NOT NULL ,
  `name` TEXT NOT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `noi_dung_1` TEXT NULL DEFAULT NULL ,
  `noi_dung_2` TEXT NULL DEFAULT NULL ,
  `hinh_1` TEXT NULL DEFAULT NULL ,
  `hinh_2` TEXT NULL DEFAULT NULL ,
  `hinh_3` TEXT NULL DEFAULT NULL ,
  `hinh_4` TEXT NULL DEFAULT NULL ,
  `hinh_5` TEXT NULL DEFAULT NULL ,
  `so_luong` INT(11) NOT NULL ,
  `gia` DOUBLE NOT NULL ,
  `gia_cu` DOUBLE NOT NULL ,
  `date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ,
  `status` VARCHAR(45) NULL DEFAULT NULL ,
  `san_phamcol` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`slide`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`slide` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `hinh_slide` TEXT NOT NULL ,
  `mo_ta` TEXT NULL DEFAULT NULL ,
  `date` DATE NULL DEFAULT NULL ,
  `status` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`ten_cuahang`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`ten_cuahang` (
  `ten_cuahang` TEXT NOT NULL ,
  `dia_chi` TEXT NOT NULL ,
  `status` TINYINT(1) NOT NULL )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `template_v2`.`tin_tuc`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `template_v2`.`tin_tuc` (
  `ten_tt` VARCHAR(45) NOT NULL ,
  `mieu_ta_tt` TEXT NULL DEFAULT NULL ,
  `hinh_tt` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`ten_tt`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

USE `template_v2` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
