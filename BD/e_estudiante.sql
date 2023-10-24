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
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `curp` varchar(18) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `paterno` varchar(50) NOT NULL,
  `materno` varchar(50) NOT NULL,
  `municipio` varchar(50) NOT NULL,
  `escuela` varchar(50) NOT NULL,
  `tramite` varchar(50) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  PRIMARY KEY (`curp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES ('','','','','','','','',''),('00000o','jos','ads','dsa','qs','dsa','qw','2132','a@dsa'),('111111111111','111111','1111111','11111111','11111111','1111','111111','111111','1111111'),('2222222','2222222','222','222222','22222','2222222','22222','2222','2222'),('23133ddsadsa','asd','as','as','a','a','a','1234322343','aa'),('323434eqwq','weq','weq','qwe','ewq','weq','wqe','12332','qwe'),('a','a','a','a','a','a','a','123','a'),('aaaaaaa','aaaaa','aaaa','aaaaaaa','aaaaaa','aaaaa','aaaaaaa','1232132','aaaaaaa'),('ads','asd','dsa','sda','asd','dsa','dsa','213232323','23'),('adsdsa','sad','ads','dsa','dsadsa','sda','dsa','232131','dsadsa'),('AIMJ9207HNLNRS07','as','a','a','a','a','a','2312312','a'),('dsa','asdsda','saddsa','sdaads','saddsa','asddsa','adsads','213231','dasdsa'),('dsadads','ads','asd','asd','asd','asd','asdads','23','dsadsa'),('dsffdssf','fdsfdsfd','dsffdsdfs','dfsfdsf','fdsfds','fdsfdsfds','fdsfds','dfsfds','fdsfdsfds'),('ewr','ewr','wer','erw','ewr','erw','sda','23312','21wqe'),('fasfdsda','adfs','eqwewq','wqe','weq','wqe','eqw','eqw','wqe'),('fds','sfd','fsd','dfs','fsd','dsf','fsd','3213212','dfs'),('GAMA930518HCMRRN02','','','','','','','',''),('GAMA930518HCMRRN03','','','','','','','',''),('GARC930615HMCRRS09','jose','adrian','ontiveros','saltillo','Jardin','Consulta','2313332','asddsadsa'),('kkkkkkkkkk','sadsdasad','sdadsasda','dsadsa','sdasda','dsadsa','dsadsa','23231','saddsasd'),('OAMJ9207HNLNRS0','luz','cara','pedra','saltillos','ads','solar','213313','as@sad'),('oekoekwrore12','asd','a','a','a','a','a','1232321','a'),('oimj920716hnlnrs0','jose','adrian','ontiveros','saltillo ','Jardin','cambiar de escuela','12332312','asda@gmail.com'),('oimj920716hnlnrs07','jose ','ontiveros','moran','saltillo','jardin','clases','1223','as@gmail.com'),('oimj920716hnlnrs12','asd','dasdsa','saddsa','sdadsa','sadsda','dasdsa','2132313','dsasda'),('OIMJ9207HNLNRS0','jose','ontiveros','moran','saltillo','jardin','Cambio','213332','adasads'),('OIMJ9207HNLNRS05','A','A','A','A','A','A','21323','A'),('OIMJ9207HNLNRS07','ASD','DAS','ADSASD','SAD','SAD','DSA','1234324','SADS'),('ooooooooo','jos','ads','dsa','qs','dsa','qw','2132','a@dsa'),('ooooooooooooooo','asd','sad','asd','das','sda','ads','13','qwe'),('OSD9207HNLNRS02','jose','ontiveros','moran','saltillo','jardin','tramite','1332332','as@gmail.com'),('osdoa','jos','ads','dsa','qs','dsa','qw','2132','a@dsa'),('PDTD800714HCLRNV02','','','','','','','',''),('PECD800714HCLRNV02','Jose','Ontiveros','Moran','Saltillo','Sistemas','Cambio de Carrera','844332438','Adrian@gmail.com'),('PETD800714HCLRNV02','','','','','','','',''),('PFTD800714HCLRNV02','Jose','Ontiveros','Moran','Saltillo','Sistemas','Cambio de Carrera','844332438','Adrian@gmail.com'),('PLTD800714HCLRNV02','','','','','','','',''),('PRTD800714HCLRNV02','','','','','','','',''),('qweqdsasad','a','a','a','a','a','a','213323','a'),('saddsa','sadsda','dasads','asddsa','dsadsa','dsadas','dsadsa','213322','adssad'),('saddsdsa','jose','sadSA','SDA','DSA','SDA','ASD','23232','SDA'),('sdffds','sdfdsf','fdsfds','dsffds','fdsfds','fdsfds','sfdfds','fdsfds','fdsfds'),('sfasfdssaf','jos','ads','dsa','qs','dsa','qw','2132','a@dsa'),('terdg34re','jose','Ontiveros','Moran','Saltillo','Jardin','cambiar localidad','844483438','a@gmail.com'),('yyyyyyyyyyy','sad','sda','dsa','das','das','dsa','12321','qwe'),('ZETD800714HCLRNV02','Jose','Ontiveros','Moran','Saltillo','Sistema','Cambio De Carrera','8443231132','Adrian@gmail.com');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-24  1:22:45
