-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: drug_manage
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--
create database drug_manage;
use drug_manage;

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `customer_name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `customer_city` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`customer_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('001','孙客户','西安'),('002','王五','西安'),('003','赵柳','北京');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug` (
  `drug_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `drug_name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `drug_level` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `drug_price` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`drug_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug`
--

LOCK TABLES `drug` WRITE;
/*!40000 ALTER TABLE `drug` DISABLE KEYS */;
INSERT INTO `drug` VALUES ('0001','布洛芬','A/B/C','34'),('0002','布洛芬','B','34'),('0003','布洛芬23','B','39'),('0004','连花清瘟','A','23'),('0005','板蓝根','C','12'),('001','阿莫西林','A','34'),('0013','布洛芬','A/B/C','15'),('002','阿莫西林','A','13'),('003','阿莫西林','A','56'),('103','阿莫西林','A','12'),('205','333333','C','121');
/*!40000 ALTER TABLE `drug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `employee_name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `employee_age` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `employee_sex` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `employee_date` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`employee_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('20220001','张三','24','男','2022/12/13'),('20220002','张天','34','男','2022/12/14'),('20220003','素素','23','男','2022/12/14'),('20220004','晶晶','44','男','2022/12/14'),('20220005','章北海','56','男','2022/12/09');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sell`
--

DROP TABLE IF EXISTS `sell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sell` (
  `sell_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `employee_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `drug_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `customer_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `warehouse_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `sell_date` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `sell_num` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `cancel` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`sell_no`),
  KEY `foreign_key_sell_employee_no` (`employee_no`),
  KEY `foreign_key_sell_drug_no` (`drug_no`),
  KEY `foreign_key_sell_customer_no` (`customer_no`),
  KEY `foreign_key_sell_warehouse_no` (`warehouse_no`),
  CONSTRAINT `foreign_key_sell_customer_no` FOREIGN KEY (`customer_no`) REFERENCES `customer` (`customer_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_sell_drug_no` FOREIGN KEY (`drug_no`) REFERENCES `drug` (`drug_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_sell_employee_no` FOREIGN KEY (`employee_no`) REFERENCES `employee` (`employee_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_sell_warehouse_no` FOREIGN KEY (`warehouse_no`) REFERENCES `warehouse` (`warehouse_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sell`
--

LOCK TABLES `sell` WRITE;
/*!40000 ALTER TABLE `sell` DISABLE KEYS */;
INSERT INTO `sell` VALUES ('0001','20220001','0001','001','001','2022/12/15','10','否'),('0002','20220002','0001','002','001','2022/12/15','10','否'),('0003','20220002','0001','002','001','2022/12/15','34','否');
/*!40000 ALTER TABLE `sell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_relation`
--

DROP TABLE IF EXISTS `store_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_relation` (
  `drug_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `warehouse_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `store_num` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`drug_no`,`warehouse_no`),
  KEY `foreign_key_store_relation_warehouse_no` (`warehouse_no`),
  CONSTRAINT `foreign_key_store_relation_drug_no` FOREIGN KEY (`drug_no`) REFERENCES `drug` (`drug_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_store_relation_warehouse_no` FOREIGN KEY (`warehouse_no`) REFERENCES `warehouse` (`warehouse_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_relation`
--

LOCK TABLES `store_relation` WRITE;
/*!40000 ALTER TABLE `store_relation` DISABLE KEYS */;
INSERT INTO `store_relation` VALUES ('0001','001','1438'),('0001','002','600');
/*!40000 ALTER TABLE `store_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `supplier_name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `supplier_city` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`supplier_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES ('001','天一','西安'),('002','正大','西安'),('003','光明','北京'),('004','往生堂','重庆');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supply_relation`
--

DROP TABLE IF EXISTS `supply_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supply_relation` (
  `supply_no` varchar(45) COLLATE utf8_bin NOT NULL,
  `drug_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `warehouse_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `supplier_no` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `supply_num` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `supply_date` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`supply_no`),
  KEY `foreign_key_supply_relation_drug_no` (`drug_no`),
  KEY `foreign_key_supply_relation_supplier_no` (`supplier_no`),
  KEY `foreign_key_supply_relation_warehouse_no` (`warehouse_no`),
  CONSTRAINT `foreign_key_supply_relation_drug_no` FOREIGN KEY (`drug_no`) REFERENCES `drug` (`drug_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_supply_relation_supplier_no` FOREIGN KEY (`supplier_no`) REFERENCES `supplier` (`supplier_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foreign_key_supply_relation_warehouse_no` FOREIGN KEY (`warehouse_no`) REFERENCES `warehouse` (`warehouse_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supply_relation`
--

LOCK TABLES `supply_relation` WRITE;
/*!40000 ALTER TABLE `supply_relation` DISABLE KEYS */;
INSERT INTO `supply_relation` VALUES ('0001','0001','001','001','301','2022/12/15'),('0002','0001','001','001','301','2022/12/15'),('0003','0001','001','001','300','2022/12/15'),('0004','0001','001','001','300','2022/12/15'),('0005','0001','001','001','300','2022/12/15'),('0006','0001','002','001','300','2022/12/15'),('0007','0001','002','001','300','2022/12/15');
/*!40000 ALTER TABLE `supply_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `warehouse_no` varchar(20) COLLATE utf8_bin NOT NULL,
  `warehouse_name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `employee_no` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `warehouse_sum` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`warehouse_no`),
  KEY `foreign_key_warehouse_employee_no` (`employee_no`),
  CONSTRAINT `foreign_key_warehouse_employee_no` FOREIGN KEY (`employee_no`) REFERENCES `employee` (`employee_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
INSERT INTO `warehouse` VALUES ('001','正和','20220002','1438'),('002','粮食A','20220001','600'),('003','正和','20220005','None');
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-16 11:43:36
