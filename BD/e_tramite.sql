CREATE DATABASE  IF NOT EXISTS `e` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `e`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: e
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `tramite`
--

DROP TABLE IF EXISTS `tramite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tramite` (
  `curp` varchar(18) NOT NULL,
  `tramite` varchar(50) NOT NULL,
  `turno` varchar(10) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `estado_tramite` varchar(50) NOT NULL,
  KEY `curp` (`curp`),
  CONSTRAINT `tramite_ibfk_1` FOREIGN KEY (`curp`) REFERENCES `estudiante` (`curp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tramite`
--

LOCK TABLES `tramite` WRITE;
/*!40000 ALTER TABLE `tramite` DISABLE KEYS */;
INSERT INTO `tramite` VALUES ('OIMJ9207HNLNRS07','SADDASSAD','2023-10-20','2023-10-20','00:51:34',''),('OIMJ9207HNLNRS05','A','2023-10-20','2023-10-20','00:52:08',''),('OSD9207HNLNRS02','tramite','20231019','2023-10-20','00:58:26',''),('fasfdsda','sdf','20231019','2023-10-20','00:59:43',''),('OIMJ9207HNLNRS0','Cambio','20231019','2023-10-20','01:12:10',''),('AIMJ9207HNLNRS07','a','20231019','2023-10-20','01:13:06',''),('OAMJ9207HNLNRS0','solar','3','2023-10-20','01:20:27',''),('ooooooooooooooo','ads','4','2023-10-20','01:21:43',''),('yyyyyyyyyyy','dsa','1','2023-10-20','01:38:34','Resolved'),('323434eqwq','wqe','2','2023-10-20','01:39:19','Pending'),('dsadads','asdads','3','2023-10-20','01:39:34','Resolved'),('oimj920716hnlnrs12','dasdsa','0','2023-10-20','03:47:40','Resolved'),('kkkkkkkkkk','dsadsa','0','2023-10-20','03:48:36','Pending'),('dsffdssf','fdsfds','1','2023-10-20','03:51:46','Resolved'),('111111111111','111111','1','2023-10-20','03:52:39','Pending'),('2222222','22222','1','2023-10-20','03:53:03','Resolved'),('sdffds','sfdfds','5555','2025-12-20','08:54:32','Resolve'),('aaaaaaa','aaaaaaa','1','2023-10-20','03:54:58','Resolved'),('saddsa','dsadsa','1','2023-10-20','04:00:56','Resolved'),('23133ddsadsa','a','1','2023-10-21','16:26:37','Resolved'),('qweqdsasad','a','0','2023-10-22','03:03:59','Resolved'),('saddsdsa','ASD','0','2023-10-22','14:48:45','Pending'),('','','0','2023-10-22','19:51:42','Pending'),('adsdsa','dsa','0','2023-10-22','19:52:02','Pending'),('ads','dsa','0','2023-10-22','22:38:29','Pending'),('fds','fsd','0','2023-10-23','00:53:55','Pending'),('PETD800714HCLRNV02','','1','2023-10-23','02:14:21','Pendiente'),('GAMA930518HCMRRN02','','0','2023-10-23','02:31:07','Pending'),('GAMA930518HCMRRN03','','0','2023-10-23','02:33:43','Pending'),('PDTD800714HCLRNV02','','0','2023-10-23','02:34:05','Resolved'),('GARC930615HMCRRS09','Consulta','0','2023-10-23','10:55:05','Pending'),('PRTD800714HCLRNV02','','0','2023-10-23','15:52:54','Pending'),('PFTD800714HCLRNV02','Cambio de Carrera','0','2023-10-23','15:54:59','Pending'),('PLTD800714HCLRNV02','','0','2023-10-23','15:58:28','Pending'),('PECD800714HCLRNV02','Cambio de Carrera','0','2023-10-23','15:59:49','Pending'),('ZETD800714HCLRNV02','Cambio De Carrera','1','2024-10-23','14:23:19','Pendiente');
/*!40000 ALTER TABLE `tramite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-24  1:22:46
