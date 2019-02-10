-- MySQL Script generated by MySQL Workbench
-- Wed Oct 31 10:23:53 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema bbTrack
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bbTrack` ;

-- -----------------------------------------------------
-- Schema bbTrack
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bbTrack` DEFAULT CHARACTER SET utf8 ;
USE `bbTrack` ;

--
-- Table structure for table `asiste_a`
--

DROP TABLE IF EXISTS `asiste_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `asiste_a` (
  `idPaciente` varchar(45) NOT NULL,
  `idConsulta` varchar(45) NOT NULL,
  `Fecha_consulta` date NOT NULL,
  `Es_urgente` tinyint(4) NOT NULL,
  `Sintomas` varchar(245) DEFAULT NULL,
  PRIMARY KEY (`idPaciente`,`idConsulta`,`Fecha_consulta`),
  KEY `fk_PACIENTE_has_CONSULTA_CONSULTA1_idx` (`idConsulta`),
  KEY `fk_PACIENTE_has_CONSULTA_PACIENTE1_idx` (`idPaciente`),
  CONSTRAINT `fk_PACIENTE_has_CONSULTA_CONSULTA1` FOREIGN KEY (`idConsulta`) REFERENCES `consulta` (`idconsulta`),
  CONSTRAINT `fk_PACIENTE_has_CONSULTA_PACIENTE1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`idpaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asiste_a`
--

LOCK TABLES `asiste_a` WRITE;
/*!40000 ALTER TABLE `asiste_a` DISABLE KEYS */;
INSERT INTO `asiste_a` VALUES ('10009','2-09-HCH','2019-04-07',0,NULL),('10725','2-02-HC','2019-01-25',0,NULL),('11194','2-02-HC','2019-01-23',0,NULL),('11470','2-09-HCH','2019-04-15',0,NULL),('14250','1-22-HC','2019-03-19',1,NULL),('15815','2-02-HC','2019-05-05',0,NULL),('15815','2-02-HC','2019-10-05',0,NULL),('15854','1-22-HC','2019-05-03',1,NULL),('15854','2-02-HC','2019-03-03',0,NULL),('17084','1-32-HCH','2019-09-07',1,NULL),('17084','2-09-HCH','2019-07-07',0,NULL),('17430','1-32-HCH','2019-05-10',1,NULL),('17785','1-22-HC','2019-03-17',1,NULL),('19198','1-32-HCH','2019-05-13',1,NULL),('19650','2-02-HC','2019-02-21',0,NULL);
/*!40000 ALTER TABLE `asiste_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atiende`
--

DROP TABLE IF EXISTS `atiende`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `atiende` (
  `idConsulta` varchar(45) NOT NULL,
  `Licencia` varchar(45) NOT NULL,
  PRIMARY KEY (`idConsulta`,`Licencia`),
  KEY `fk_CONSULTA_has_MEDICO_MEDICO1_idx` (`Licencia`),
  KEY `fk_CONSULTA_has_MEDICO_CONSULTA1_idx` (`idConsulta`),
  CONSTRAINT `fk_CONSULTA_has_MEDICO_CONSULTA1` FOREIGN KEY (`idConsulta`) REFERENCES `consulta` (`idconsulta`),
  CONSTRAINT `fk_CONSULTA_has_MEDICO_MEDICO1` FOREIGN KEY (`Licencia`) REFERENCES `medico` (`licencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atiende`
--

LOCK TABLES `atiende` WRITE;
/*!40000 ALTER TABLE `atiende` DISABLE KEYS */;
INSERT INTO `atiende` VALUES ('1-22-HC','M-10938'),('2-02-HC','M-23444'),('2-09-HCH','M-23494'),('1-22-HC','M-32349'),('2-09-HCH','M-33048'),('2-02-HC','M-43434'),('2-02-HC','M-98488'),('1-32-HCH','M-99432');
/*!40000 ALTER TABLE `atiende` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Consulta`
--

DROP TABLE IF EXISTS `Consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Consulta` (
  `idConsulta` varchar(45) NOT NULL,
  `Localizacion` varchar(125) NOT NULL,
  `Centro_sanitario` varchar(45) NOT NULL,
  PRIMARY KEY (`idConsulta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consulta`
--

LOCK TABLES `Consulta` WRITE;
/*!40000 ALTER TABLE `Consulta` DISABLE KEYS */;
INSERT INTO `Consulta` VALUES ('1-22-HC','Primera planta. Puerta 22','Hospital Clinico'),('1-32-HCH','Primera planta. Puerta 32','Hospital Carlos Haya'),('2-02-HC','Segunda planta. Puerta 2','Hospital Clinico'),('2-09-HCH','Segunda planta. Puerta 09','Hospital Carlos Haya');
/*!40000 ALTER TABLE `Consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `es_atendido`
--

DROP TABLE IF EXISTS `es_atendido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `es_atendido` (
  `idPaciente` varchar(45) NOT NULL,
  `Licencia` varchar(45) NOT NULL,
  PRIMARY KEY (`Licencia`,`idPaciente`),
  KEY `fk_PACIENTE_has_MEDICO_MEDICO1_idx` (`Licencia`),
  KEY `fk_PACIENTE_has_MEDICO_PACIENTE1_idx` (`idPaciente`),
  CONSTRAINT `fk_PACIENTE_has_MEDICO_MEDICO1` FOREIGN KEY (`Licencia`) REFERENCES `medico` (`licencia`),
  CONSTRAINT `fk_PACIENTE_has_MEDICO_PACIENTE1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`idpaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `es_atendido`
--

LOCK TABLES `es_atendido` WRITE;
/*!40000 ALTER TABLE `es_atendido` DISABLE KEYS */;
INSERT INTO `es_atendido` VALUES ('15854','M-10938'),('17785','M-10938'),('11194','M-23444'),('15815','M-23444'),('11470','M-23494'),('17084','M-23494'),('14250','M-32349'),('10009','M-33048'),('10725','M-43434'),('15815','M-43434'),('15854','M-98488'),('19560','M-98488'),('17084','M-99432'),('17430','M-99432'),('19198','M-99432');
/*!40000 ALTER TABLE `es_atendido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FACTOR_DE_RIESGO_PRENATAL`
--

DROP TABLE IF EXISTS `FACTOR_DE_RIESGO_PRENATAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `FACTOR_DE_RIESGO_PRENATAL` (
  `Antecedentes_familiares` varchar(245) DEFAULT NULL,
  `Factores_psicosociales` varchar(245) DEFAULT NULL,
  `Antecedentes_obstetricos` varchar(245) DEFAULT NULL,
  `Antecedentes_personales` varchar(245) DEFAULT NULL,
  `Patologia_materna` varchar(245) DEFAULT NULL,
  `Riesgos_especificos` varchar(245) DEFAULT NULL,
  `Exposicion_a_teratogenos` varchar(245) DEFAULT NULL,
  `idHistorial` varchar(45) NOT NULL,
  KEY `fk_FACTOR DE RIESGO PRENATAL_HISTORIAL1_idx` (`idHistorial`),
  CONSTRAINT `fk_FACTOR DE RIESGO PRENATAL_HISTORIAL1` FOREIGN KEY (`idHistorial`) REFERENCES `historial` (`idhistorial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FACTOR_DE_RIESGO_PRENATAL`
--

LOCK TABLES `FACTOR_DE_RIESGO_PRENATAL` WRITE;
/*!40000 ALTER TABLE `FACTOR_DE_RIESGO_PRENATAL` DISABLE KEYS */;
INSERT INTO `FACTOR_DE_RIESGO_PRENATAL` VALUES ('Hipertensión arterial','Tabaco','muerte neonatal anterior',NULL,'Hipertensión arterial','Gestacion multiple',NULL,'H-15815'),('Diabetes','Tabaco','aborto','diabetes','Diabetes gestacional','Amenaza de parto pretérmino','Fármacos','H-15854'),('Presencia de cromosomopatias','47 años','aborto','Obesidad. (IMC>27%)',NULL,'Amenaza de parto pretérmino',NULL,'H-17084'),(NULL,'40 años','Historia de infertilidad de al menos 2 años','diabetes',NULL,NULL,'Fármacos','H-10725'),('Diabetes',NULL,'muerte neonatal anterior','Obesidad. (IMC>27%)','Anemia','Estática fetal anómala pasada la semana 36',NULL,'H-11194'),('Hipertensión arterial','45 años','Historia de infertilidad de al menos 2 años',NULL,NULL,'Embarazo prolongado','Fármacos','H-19560'),(NULL,'Drogas','aborto','V.I.H',NULL,NULL,NULL,'H-14250'),(NULL,'38 años','muerte neonatal anterior','diabetes','Anemia','Estática fetal anómala pasada la semana 36','Fármacos','H-17785'),('Diabetes','Tabaco','aborto',NULL,'Diabetes gestacional','Embarazo prolongado',NULL,'H-11470'),(NULL,'47 años','muerte neonatal anterior',NULL,NULL,NULL,'Fármacos','H-10009'),('Presencia de cromosomopatias',NULL,'Historia de infertilidad de al menos 2 años','V.I.H','Diabetes gestacional',NULL,'Fármacos','H-19198'),('Hipertensión arterial','Tabaco','muerte neonatal anterior',NULL,'Diabetes gestacional',NULL,NULL,'H-17430');
/*!40000 ALTER TABLE `FACTOR_DE_RIESGO_PRENATAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Historial`
--

DROP TABLE IF EXISTS `Historial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Historial` (
  `idHistorial` varchar(45) NOT NULL,
  `Fecha_primera_consulta` date NOT NULL,
  `idPaciente` varchar(45) NOT NULL,
  `Vacunas` varchar(245) DEFAULT NULL,
  PRIMARY KEY (`idHistorial`),
  KEY `fk_HISTORIAL_PACIENTE1_idx` (`idPaciente`),
  CONSTRAINT `fk_HISTORIAL_PACIENTE1` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`idpaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Historial`
--

LOCK TABLES `Historial` WRITE;
/*!40000 ALTER TABLE `Historial` DISABLE KEYS */;
INSERT INTO `Historial` VALUES ('H-10009','2019-04-07','10009',NULL),('H-10725','2019-01-25','10725',NULL),('H-11194','2019-02-23','11194',NULL),('H-11470','2019-04-15','11470',NULL),('H-14250','2019-03-19','14250',NULL),('H-15815','2019-05-05','15815',NULL),('H-15854','2019-03-03','15854',NULL),('H-17084','2019-07-07','17084',NULL),('H-17430','2019-05-10','17430',NULL),('H-17785','2019-03-17','17785',NULL),('H-19198','2019-05-13','19198',NULL),('H-19560','2019-02-21','19560',NULL);
/*!40000 ALTER TABLE `Historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ICD_10`
--

DROP TABLE IF EXISTS `ICD_10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ICD_10` (
  `Codigo` varchar(45) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ICD_10`
--

LOCK TABLES `ICD_10` WRITE;
/*!40000 ALTER TABLE `ICD_10` DISABLE KEYS */;
INSERT INTO `ICD_10` VALUES ('D70.1','Agranulocytosis secondary to cancer chemotherapy'),('D86.0','Sarcoidosis of lung'),('J67.0','Farmer\'s lung'),('J67.2','Bird fancier\'s lung'),('J67.4','Maltworker\'s lung'),('O00.1','Ectopic pregnancy'),('O00.2','Hydatidiform mole'),('O02.2','Other abnormal products of conception'),('O02.3','Spontaneous abortion'),('O04.3','Medical abortion'),('O05.4','Other abortion'),('O06.3','Unspecified abortion'),('O10.3','Pre-existing hypertension complicating pregnancy, childbirth and the puerperium'),('O11.1','Pre-existing hypertensive disorder with superimposed proteinuria'),('R97.1','Elevated cancer antigen 125 [CA 125]'),('T80.51XS','Anaphylactic reaction due to administration of blood and blood products, sequela'),('Z52.090','Other blood donor, whole blood'),('Z52.098','Other blood donor, other blood');
/*!40000 ALTER TABLE `ICD_10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Informe`
--

DROP TABLE IF EXISTS `Informe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Informe` (
  `idInforme` varchar(45) NOT NULL,
  `Estado_paciente` varchar(45) NOT NULL,
  `Diagnostico` varchar(255) NOT NULL,
  `idHistorial` varchar(45) NOT NULL,
  `Fecha_consulta` date NOT NULL,
  `idConsulta` varchar(45) NOT NULL,
  `Licencia_medico` varchar(45) NOT NULL,
  PRIMARY KEY (`idInforme`,`idConsulta`,`Licencia_medico`),
  KEY `fk_INFORME_HISTORIAL1_idx` (`idHistorial`),
  KEY `fk_INFORME_CONSULTA1_idx` (`idConsulta`),
  KEY `fk_INFORME_MEDICO1_idx` (`Licencia_medico`),
  CONSTRAINT `fk_INFORME_CONSULTA1` FOREIGN KEY (`idConsulta`) REFERENCES `consulta` (`idconsulta`),
  CONSTRAINT `fk_INFORME_HISTORIAL1` FOREIGN KEY (`idHistorial`) REFERENCES `historial` (`idhistorial`),
  CONSTRAINT `fk_INFORME_MEDICO1` FOREIGN KEY (`Licencia_medico`) REFERENCES `medico` (`licencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Informe`
--

LOCK TABLES `Informe` WRITE;
/*!40000 ALTER TABLE `Informe` DISABLE KEYS */;
INSERT INTO `Informe` VALUES ('H-10009-209HCH-190204','Estable','Analisis correcto','H-10009','2019-02-04','2-09-HCH','M-10938'),('H-10009-209HCH-190407','Estable','Seguimiento embarazo de alto riesgo. Solicita prueba cariotipo','H-10009','2019-04-07','2-09-HCH','M-33048'),('H-10725-202HC-190125','Estable','El paciente solicita prueba de esterilidad','H-10725','2019-01-25','2-02-HC','M-43434'),('H-11194-202HC-190123','Grave estable','Malestar estomacal debido a un virus','H-11194','2019-01-23','2-02-HC','M-23444'),('H-11470-202HC-190204','Grave inestable','adf','H-11470','2019-02-04','2-02-HC','M-10938'),('H-11470-209HCH-190415','Estable','El paciente solicita prueba de esterilidad','H-11470','2019-04-15','2-09-HCH','M-23494'),('H-14250-122HC-190319','Estable','Esguince de primer grado','H-14250','2019-03-19','1-22-HC','M-32349'),('H-15815-202HC-190505','Estable','El paciente ha intentado quedarse embarazada y no procede. Se solicita cita con especialista','H-15815','2019-05-05','2-02-HC','M-43434'),('H-15815-202HC-191005','Estable','Se solicita analisis de sangre','H-15815','2019-10-05','2-02-HC','M-23444'),('H-15854-202HC-190303','Estable','Prueba rutinaria completada','H-15854','2019-03-03','2-02-HC','M-98488'),('H-17084-132HCH-190907','Grave estable','Anginas','H-17084','2019-09-07','1-32-HCH','M-99432'),('H-17084-209HCH-190707','Estable','Prueba rutinaria compleada','H-17084','2019-07-07','2-09-HCH','M-23494'),('H-17430-132HCH-190510','Estable','El paciente solicita prueba de esterilidad','H-17430','2019-05-10','1-32-HCH','M-99432'),('H-17430-209HCH-190204','Grave estable','Analisis','H-17430','2019-02-04','2-09-HCH','M-10938'),('H-17785-122HC-190317','Grave estable','Solicitud de prueba de sangre debido a desmayo','H-17785','2019-03-17','1-22-HC','M-10938'),('H-19198-132HCH-190513','Grave inestable','Ingreso en Hospital debido a brote de V.I.H','H-19198','2019-05-13','1-32-HCH','M-99432'),('H-19650-202HC-190221','Estable','Seguimiento por embarazo de riesgo','H-19650','2019-02-21','2-02-HC','M-98488');
/*!40000 ALTER TABLE `Informe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INFORME_ICD_10`
--

DROP TABLE IF EXISTS `INFORME_ICD_10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `INFORME_ICD_10` (
  `Codigo` varchar(45) NOT NULL,
  `IdInforme` varchar(45) NOT NULL,
  KEY `fk_ICD-10_has_INFORME_INFORME1_idx` (`IdInforme`),
  KEY `fk_ICD-10_has_INFORME_ICD-101_idx` (`Codigo`),
  CONSTRAINT `fk_ICD-10_has_INFORME_ICD-101` FOREIGN KEY (`Codigo`) REFERENCES `icd_10` (`codigo`),
  CONSTRAINT `fk_ICD-10_has_INFORME_INFORME1` FOREIGN KEY (`IdInforme`) REFERENCES `informe` (`idinforme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INFORME_ICD_10`
--

LOCK TABLES `INFORME_ICD_10` WRITE;
/*!40000 ALTER TABLE `INFORME_ICD_10` DISABLE KEYS */;
INSERT INTO `INFORME_ICD_10` VALUES ('O00.1','H-15815-202HC-190505'),('O00.2','H-15815-202HC-191005'),('O00.1','H-15854-202HC-190303'),('O00.2','H-15854-122HC-190503'),('O05.4','H-17084-209HCH-190707'),('O05.4','H-17084-132HCH-190907'),('O05.4','H-10725-202HC-190125'),('O06.3','H-11194-202HC-190123'),('O06.3','H-19650-202HC-190221'),('O00.1','H-14250-122HC-190319'),('O00.1','H-17785-122HC-190317'),('O11.1','H-11470-209HCH-190415'),('O10.3','H-10009-209HCH-190407'),('O10.3','H-19198-132HCH-190513'),('O05.4','H-17430-132HCH-190510'),('O11.1','H-15815-202HC-190505'),('O05.4','H-15815-202HC-191005'),('O10.3','H-15854-202HC-190303'),('O11.1','H-15854-122HC-190503'),('O05.4','H-17084-209HCH-190707'),('O05.4','H-17084-132HCH-190907'),('O05.4','H-10725-202HC-190125'),('O00.2','H-11194-202HC-190123'),('O00.2','H-11470-209HCH-190415'),('O02.3','H-10009-209HCH-190407'),('O02.3','H-19198-132HCH-190513'),('O00.2','H-17430-132HCH-190510'),('O00.1','H-15815-202HC-190505'),('O02.3','H-15815-202HC-191005'),('O00.2','H-15854-202HC-190303'),('O00.2','H-15854-122HC-190503'),('O00.2','H-17084-209HCH-190707'),('O02.3','H-17084-132HCH-190907'),('O11.1','H-10725-202HC-190125'),('O11.1','H-11194-202HC-190123'),('Z52.090','H-10009-209HCH-190204'),('T80.51XS','H-10009-209HCH-190204'),('Z52.098','H-10009-209HCH-190204'),('O04.3','H-10009-209HCH-190204'),('O00.2','H-10009-209HCH-190204'),('O02.3','H-10009-209HCH-190204'),('J67.0','H-10009-209HCH-190204'),('O02.3','H-11470-202HC-190204'),('J67.0','H-11470-202HC-190204'),('D70.1','H-11470-202HC-190204'),('R97.1','H-11470-202HC-190204'),('D86.0','H-17430-209HCH-190204'),('J67.4','H-17430-209HCH-190204'),('J67.2','H-17430-209HCH-190204'),('R97.1','H-17430-209HCH-190204'),('D70.1','H-17430-209HCH-190204'),('O00.1','H-17430-209HCH-190204'),('O00.2','H-17430-209HCH-190204'),('O04.3','H-17430-209HCH-190204'),('O05.4','H-17430-209HCH-190204');
/*!40000 ALTER TABLE `INFORME_ICD_10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medico`
--

DROP TABLE IF EXISTS `Medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Medico` (
  `Licencia` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellidos` varchar(45) NOT NULL,
  `Sexo` enum('Hombre','Mujer') NOT NULL,
  `Especialidad` varchar(45) NOT NULL,
  PRIMARY KEY (`Licencia`),
  KEY `Apellido` (`Apellidos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medico`
--

LOCK TABLES `Medico` WRITE;
/*!40000 ALTER TABLE `Medico` DISABLE KEYS */;
INSERT INTO `Medico` VALUES ('M-10938','Antonio','Jurado Martos','Hombre','Urgencias'),('M-23444','Miguel','Perez Jimenez','Hombre','Ginecologia'),('M-23494','Lucia','Toscano Varela','Mujer','Obstetra'),('M-32349','Paloma','Jimenez Fernandez','Mujer','Ginecologia'),('M-33048','Laura','Lara Ruiz','Mujer','Medico de familia'),('M-43434','Enrique','Barbarela Benitez','Hombre','Medico de familia'),('M-98488','Juan','Serrano Lopez','Hombre','Obstetra'),('M-99432','Maria','Pastor Smith','Mujer','Urgencias');
/*!40000 ALTER TABLE `Medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Paciente` (
  `idPaciente` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `NUSS` varchar(45) NOT NULL,
  `Sexo` enum('Hombre','Mujer') NOT NULL,
  `Fecha_nacimiento` date NOT NULL,
  `Localidad` varchar(45) NOT NULL,
  `Domicilio` varchar(45) NOT NULL,
  `Apellidos` varchar(45) NOT NULL,
  `Telefono` varchar(13) DEFAULT NULL,
  `Correo_electronico` varchar(45) DEFAULT NULL,
  `Embarazada` tinyint(4) NOT NULL,
  `FPP` date DEFAULT NULL,
  PRIMARY KEY (`idPaciente`),
  UNIQUE KEY `NUSS_UNIQUE` (`NUSS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
INSERT INTO `Paciente` VALUES ('10009','Carmen','AN-10009','Mujer','1998-03-04','Malaga','Malaga','Benitez Amancio','769154260','carmenBn@bbtrack.es',1,'2019-02-05'),('10725','Leticia','AN-10725','Mujer','1996-12-01','Malaga','C/Tintoreria 48','Lara Benitez','627529703','leticiaLr@bbtrack.es',1,'2019-12-01'),('11194','Leyre','AN-11194','Mujer','1992-11-12','Malaga','C/Union 49','Trujillo Ruiz','691632540','leyreTu@bbtrack.es',1,'2019-11-12'),('11470','Inmaculada','AN-11470','Mujer','1997-03-03','Malaga','C/Malagueta 53','Valera Trujillo','601529436','inmaculadaVl@bbtrack.es',0,NULL),('11529','Dorotea','AN-11529','Mujer','1997-03-10','Malaga','C/Joaquin 60','Buendia Calzado','729626220','doroteaBe@bbtrack.es',1,'2019-03-10'),('12288','Dolores','AN-12288','Mujer','1997-03-08','Alhaurin de la Torre','C/Torres 58','Ruiz Calzado','627550890','doloresRi@bbtrack.es',1,'2019-03-08'),('14250','Almudena','AN-14250','Mujer','1989-12-05','Malaga','C/Vicente 51','Asensio Maside','654555531','almudenaAe@bbtrack.es',1,'2019-12-05'),('15815','Maria','AN-15815','Mujer','1997-12-20','Malaga','C/Lucena 45','Lopez Perez','724444896','mariaLp@bbtrack.es',0,NULL),('15854','Araceli','AN-15854','Mujer','1980-12-10','Malaga','C/Julio de Tormes 46','Toscano Medina','637565322','araceliTs@bbtrack.es',1,'2019-12-10'),('17084','Celia','AN-17084','Mujer','1990-02-12','Malaga','C/Torremolinos 47','Del Bosque Santaella','761635888','celiaDl@bbtrack.es',1,'2019-02-12'),('17430','Paloma','AN-17430','Mujer','1997-07-24','Alhaurin de la Torre','C/Cordoba 56','Amancio Ortega','751849297','palomaAa@bbtrack.es',0,NULL),('17785','Maria','AN-17785','Mujer','1998-01-01','Malaga','C/Andalucia 52','Quiroga Lopez','685047012','mariaQi@bbtrack.es',1,'2019-01-01'),('18616','Estrella','AN-19616','Mujer','1990-03-07','Alhaurin de la Torre','C/Lucena 57','Gonzalez Blanco','729843321','estrellaGn@bbtrack.es',0,NULL),('19198','Violeta','AN-19198','Mujer','1993-05-05','Malaga','C/Juego de pelota 55','Lara Cruz','663240005','violetaLr@bbtrack.es',1,'2019-05-05'),('19560','Sara','AN-19560','Mujer','1991-12-12','Malaga','C/Larios 50','Garcia Molero','704293198','saraGr@bbtrack.es',1,'2019-12-12');
/*!40000 ALTER TABLE `Paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prueba`
--

DROP TABLE IF EXISTS `Prueba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Prueba` (
  `idPrueba` varchar(45) NOT NULL,
  `Observaciones` varchar(255) NOT NULL,
  `idPrueba_externo` varchar(45) NOT NULL,
  `Tipo` enum('Rutinaria','Especial') NOT NULL,
  `idInforme` varchar(45) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`idPrueba`),
  UNIQUE KEY `IdPrueba_externo_UNIQUE` (`idPrueba_externo`),
  KEY `Tipo` (`Tipo`),
  KEY `fk_PRUEBA_INFORME1_idx` (`idInforme`),
  CONSTRAINT `fk_PRUEBA_INFORME1` FOREIGN KEY (`idInforme`) REFERENCES `informe` (`idinforme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prueba`
--

LOCK TABLES `Prueba` WRITE;
/*!40000 ALTER TABLE `Prueba` DISABLE KEYS */;
INSERT INTO `Prueba` VALUES ('12','Bien','P-H-10009-209HCH-190204-12','Rutinaria','H-10009-209HCH-190204','Analisis de sangre'),('13','Ok','P-H-10009-209HCH-190204-13','Especial','H-10009-209HCH-190204','Amniocentesis'),('14','adf','P-H-11470-202HC-190204-14','Rutinaria','H-11470-202HC-190204','adf'),('15','asdf','P-H-17430-209HCH-190204-15','Rutinaria','H-17430-209HCH-190204','Analisis'),('16','Correcto','P-H-17430-209HCH-190204-16','Rutinaria','H-17430-209HCH-190204','Aminiocentesis'),('P-1','Todo correcto','P-15854-202HC-190303-1','Rutinaria','H-15854-202HC-190303','Analisis de sangre'),('P-10','Todo correcto','P-10009-209HCH-190407','Rutinaria','H-10009-209HCH-190407','Cariotipo'),('P-11','Todo correcto','P-17430-132HCH-190510','Especial','H-17430-132HCH-190510','Histeroscopia'),('P-2','Toco correcto','P-17084-209HCH-190707-1','Rutinaria','H-17084-209HCH-190707','Analisis de orina'),('P-3','Todo correcto','P-15854-202HC-190303-2','Especial','H-15854-202HC-190303','Amniocentesis'),('P-4','Toco correcto','P-17084-209HCH-190707-2','Rutinaria','H-17084-209HCH-190707','Ecografia'),('P-5','Anemia','P-15815-202HC-191005','Rutinaria','H-15815-202HC-191005','Analisis de sangre'),('P-6','Todo correcto','P-10725-202HC-190125','Especial','H-10725-202HC-190125','Ecografia transvaginal'),('P-7','Trisomia','P-19650-202HC-190221','Rutinaria','H-19650-202HC-190221','Cariotipo'),('P-8','Esguince de primer grado','P-14250-122HC-190319','Especial','H-14250-122HC-190319','Radiografia'),('P-9','Lesion en las trompas de falopio','P-11470-209HCH-190415','Especial','H-11470-209HCH-190415','Ecografia transvaginal');
/*!40000 ALTER TABLE `Prueba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Usuario` (
  `idUsuario` varchar(45) NOT NULL,
  `PSS` varchar(45) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  KEY `fk_Usuario_Medico1_idx` (`idUsuario`),
  CONSTRAINT `fk_Usuario_Medico1` FOREIGN KEY (`idUsuario`) REFERENCES `medico` (`licencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES ('M-10938','P10938'),('M-23444','P23444'),('M-23494','P23494'),('M-32349','P32349'),('M-33048','P33048'),('M-43434','P43434'),('M-98488','P98488'),('M-99432','P99432');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-05  0:03:56