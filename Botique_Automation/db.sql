/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - django_mariyan_boutique
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`boutique` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `boutique`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add booking',7,'add_booking'),
(26,'Can change booking',7,'change_booking'),
(27,'Can delete booking',7,'delete_booking'),
(28,'Can view booking',7,'view_booking'),
(29,'Can add category',8,'add_category'),
(30,'Can change category',8,'change_category'),
(31,'Can delete category',8,'delete_category'),
(32,'Can view category',8,'view_category'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add user',10,'add_user'),
(38,'Can change user',10,'change_user'),
(39,'Can delete user',10,'delete_user'),
(40,'Can view user',10,'view_user'),
(41,'Can add payment',11,'add_payment'),
(42,'Can change payment',11,'change_payment'),
(43,'Can delete payment',11,'delete_payment'),
(44,'Can view payment',11,'view_payment'),
(45,'Can add design',12,'add_design'),
(46,'Can change design',12,'change_design'),
(47,'Can delete design',12,'delete_design'),
(48,'Can view design',12,'view_design'),
(49,'Can add customised_design',13,'add_customised_design'),
(50,'Can change customised_design',13,'change_customised_design'),
(51,'Can delete customised_design',13,'delete_customised_design'),
(52,'Can view customised_design',13,'view_customised_design'),
(53,'Can add bchild',14,'add_bchild'),
(54,'Can change bchild',14,'change_bchild'),
(55,'Can delete bchild',14,'delete_bchild'),
(56,'Can view bchild',14,'view_bchild'),
(57,'Can add cpayment',15,'add_cpayment'),
(58,'Can change cpayment',15,'change_cpayment'),
(59,'Can delete cpayment',15,'delete_cpayment'),
(60,'Can view cpayment',15,'view_cpayment'),
(61,'Can add purchase',16,'add_purchase'),
(62,'Can change purchase',16,'change_purchase'),
(63,'Can delete purchase',16,'delete_purchase'),
(64,'Can view purchase',16,'view_purchase'),
(65,'Can add chat',17,'add_chat'),
(66,'Can change chat',17,'change_chat'),
(67,'Can delete chat',17,'delete_chat'),
(68,'Can view chat',17,'view_chat'),
(69,'Can add sizechart',18,'add_sizechart'),
(70,'Can change sizechart',18,'change_sizechart'),
(71,'Can delete sizechart',18,'delete_sizechart'),
(72,'Can view sizechart',18,'view_sizechart'),
(73,'Can add feedback',19,'add_feedback'),
(74,'Can change feedback',19,'change_feedback'),
(75,'Can delete feedback',19,'delete_feedback'),
(76,'Can view feedback',19,'view_feedback'),
(77,'Can add refer_no',20,'add_refer_no'),
(78,'Can change refer_no',20,'change_refer_no'),
(79,'Can delete refer_no',20,'delete_refer_no'),
(80,'Can view refer_no',20,'view_refer_no'),
(81,'Can add wishlist',21,'add_wishlist'),
(82,'Can change wishlist',21,'change_wishlist'),
(83,'Can delete wishlist',21,'delete_wishlist'),
(84,'Can view wishlist',21,'view_wishlist');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `bouti_bchild` */

DROP TABLE IF EXISTS `bouti_bchild`;

CREATE TABLE `bouti_bchild` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `qty` varchar(225) NOT NULL,
  `bamt` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  `design_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_bchild_booking_id_0f56263c` (`booking_id`),
  KEY `bouti_bchild_design_id_99c2bfd7` (`design_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_bchild` */

insert  into `bouti_bchild`(`id`,`qty`,`bamt`,`booking_id`,`design_id`) values 
(15,'2','2000',13,5),
(14,'4','4000',13,6),
(13,'12','12000',3,6),
(12,'2','100',14,4),
(16,'2','2000',14,6);

/*Table structure for table `bouti_booking` */

DROP TABLE IF EXISTS `bouti_booking`;

CREATE TABLE `bouti_booking` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `sizechart_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_booking_user_id_db6679db` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_booking` */

insert  into `bouti_booking`(`id`,`total`,`date`,`status`,`user_id`,`sizechart_id`) values 
(1,'3000','20-12-2023','dispatched',1,0),
(2,'6000','2023-02-03','dispatched',2,0),
(3,'9000','2023-02-03','paid',2,0),
(4,'6000','2023-02-16','dispatched',1,0),
(5,'3000','2023-02-16','paid',1,0),
(6,'13400','2023-02-17','paid',1,0),
(9,'6700','2023-02-18','paid',1,3),
(10,'20100','2023-02-18','paid',1,3),
(11,'13400','2023-02-18','paid',1,1),
(12,'10000','2023-02-20','pending',1,1),
(13,'6000','2023-03-04','paid',2,1),
(14,'2000','2023-03-04','cancelled',2,6);

/*Table structure for table `bouti_category` */

DROP TABLE IF EXISTS `bouti_category`;

CREATE TABLE `bouti_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_category` */

insert  into `bouti_category`(`id`,`category`) values 
(3,'dress');

/*Table structure for table `bouti_chat` */

DROP TABLE IF EXISTS `bouti_chat`;

CREATE TABLE `bouti_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `chat` varchar(225) NOT NULL,
  `reply` varchar(225) NOT NULL,
  `date` varchar(1000) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_chat_user_id_fe2ed5f6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_chat` */

insert  into `bouti_chat`(`id`,`chat`,`reply`,`date`,`user_id`) values 
(1,'hiiii','dghy','2023-02-03',2),
(2,'jjj','fish','2023-02-16',1),
(3,'tfyg','pending','2023-02-17',1),
(4,'kkkkk','pending','2023-02-20',1),
(5,'kkkkkk','pending','2023-02-20',1);

/*Table structure for table `bouti_cpayment` */

DROP TABLE IF EXISTS `bouti_cpayment`;

CREATE TABLE `bouti_cpayment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `camount` varchar(225) NOT NULL,
  `cdate` varchar(225) NOT NULL,
  `customised_design_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_cpayment_customised_design_id_1e30c152` (`customised_design_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_cpayment` */

insert  into `bouti_cpayment`(`id`,`camount`,`cdate`,`customised_design_id`) values 
(1,'100','20-10-2023',1),
(2,'100','2023-02-03',2);

/*Table structure for table `bouti_customised_design` */

DROP TABLE IF EXISTS `bouti_customised_design`;

CREATE TABLE `bouti_customised_design` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(225) NOT NULL,
  `cd_name` varchar(225) NOT NULL,
  `details` varchar(225) DEFAULT NULL,
  `amount` varchar(225) NOT NULL,
  `date` varchar(1000) NOT NULL,
  `status` varchar(2000) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `orderid` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_customised_design_user_id_3c470f11` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_customised_design` */

insert  into `bouti_customised_design`(`id`,`quantity`,`cd_name`,`details`,`amount`,`date`,`status`,`user_id`,`orderid`) values 
(1,'1','34',NULL,'100','20-01-2023','reject',1,NULL),
(2,'2','34',NULL,'pending','2023-02-03','accept',2,NULL),
(3,'2','small',NULL,'50','2023-02-17','paid',1,''),
(4,'2','churidar','qwertyuijkl','pending','2023-02-18','pending',1,''),
(5,'4','s','kkmk','pending','2023-02-20','pending',1,'');

/*Table structure for table `bouti_design` */

DROP TABLE IF EXISTS `bouti_design`;

CREATE TABLE `bouti_design` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `design` varchar(225) NOT NULL,
  `dqty` varchar(225) NOT NULL,
  `amount` varchar(225) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `details` varchar(2000) NOT NULL,
  `category_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_design_category_id_9d0224e7` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_design` */

insert  into `bouti_design`(`id`,`design`,`dqty`,`amount`,`image`,`details`,`category_id`) values 
(4,'njnj','102','100','tapan-kumar-choudhury-YNHBcAabHUQ-unsplash.jpg','uhyhyyhyhhy',3),
(5,'top','38','1000','erica-zhou-IHpUgFDn7zU-unsplash (1).jpg','qwertyuiop',3),
(6,'kurthi','98','1000','pexels-jill-wellington-5618793_fZDeMQU.jpg','sdfrtgy dfgh',3);

/*Table structure for table `bouti_feedback` */

DROP TABLE IF EXISTS `bouti_feedback`;

CREATE TABLE `bouti_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_feedback_user_id_58c80fc5` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_feedback` */

insert  into `bouti_feedback`(`id`,`feedback`,`date`,`user_id`) values 
(1,'good','2023-02-17',1);

/*Table structure for table `bouti_login` */

DROP TABLE IF EXISTS `bouti_login`;

CREATE TABLE `bouti_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_login` */

insert  into `bouti_login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'ammu','ammu','user'),
(4,'anju','12345678','user'),
(5,'','','user'),
(6,'appu','1234','pending'),
(7,'annababykpe@gmail.com','09876543','user'),
(8,'annababykp@gmail.com','1234','pending'),
(11,'kanchana','12345678','user');

/*Table structure for table `bouti_payment` */

DROP TABLE IF EXISTS `bouti_payment`;

CREATE TABLE `bouti_payment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_payment_booking_id_90722068` (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_payment` */

insert  into `bouti_payment`(`id`,`amount`,`date`,`booking_id`) values 
(1,'3000','20-12-2023',1),
(2,'6000','2023-02-03',2),
(3,'6000','2023-02-16',4);

/*Table structure for table `bouti_purchase` */

DROP TABLE IF EXISTS `bouti_purchase`;

CREATE TABLE `bouti_purchase` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(225) NOT NULL,
  `amount` varchar(225) NOT NULL,
  `date` varchar(1000) NOT NULL,
  `details` varchar(2000) DEFAULT NULL,
  `design_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_purchase_design_id_138b448d` (`design_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_purchase` */

insert  into `bouti_purchase`(`id`,`quantity`,`amount`,`date`,`details`,`design_id`) values 
(2,'100','1000','2023-02-20','oko',4);

/*Table structure for table `bouti_refer_no` */

DROP TABLE IF EXISTS `bouti_refer_no`;

CREATE TABLE `bouti_refer_no` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `refer_no` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `booking_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_refer_no_booking_id_64c1a8c0` (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_refer_no` */

insert  into `bouti_refer_no`(`id`,`refer_no`,`date`,`booking_id`) values 
(1,'123456789','2023-02-18',5),
(2,'Carrier Station Road, Ernakulam-South, Kochi, Kerala 682011 ','2023-03-04',13);

/*Table structure for table `bouti_sizechart` */

DROP TABLE IF EXISTS `bouti_sizechart`;

CREATE TABLE `bouti_sizechart` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `size` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `design_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_sizechart` */

insert  into `bouti_sizechart`(`id`,`size`,`status`,`design_id`) values 
(1,'large','deactive',5),
(3,'small','active',5),
(4,'xxl','active',5),
(5,'large','active',6),
(6,'none','active',6);

/*Table structure for table `bouti_user` */

DROP TABLE IF EXISTS `bouti_user`;

CREATE TABLE `bouti_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `address` varchar(225) NOT NULL,
  `login_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bouti_user_login_id_5fd3e2af` (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_user` */

insert  into `bouti_user`(`id`,`fname`,`lname`,`place`,`phone`,`email`,`address`,`login_id`) values 
(1,'Ammu','kumar','kochi','9988776650','ammu@gmail.com','qwertyui',3),
(2,'anju','s','kochi','9934776611','shivanjanam84@gmail.com','SDFGHJUKIUK',4),
(3,'','','','','','',5),
(4,'aparna','s','kochi','9934776611','shivanjanam84@gmail.com','ertyui',6),
(5,'aparna','s','kochi','9934776611','annababykp@gmail.com','687651',7),
(6,'lakshmi','swami','kozhikode','8877665544','annababykp@gmail.com','678999ertyu',8),
(7,'kanchana','s','kottayam','6238621692','kanchanasnair2018@gmail.com','purathuttu',11);

/*Table structure for table `bouti_wishlist` */

DROP TABLE IF EXISTS `bouti_wishlist`;

CREATE TABLE `bouti_wishlist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `design_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bouti_wishlist` */

insert  into `bouti_wishlist`(`id`,`design_id`,`user_id`) values 
(3,4,1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'bouti','booking'),
(8,'bouti','category'),
(9,'bouti','login'),
(10,'bouti','user'),
(11,'bouti','payment'),
(12,'bouti','design'),
(13,'bouti','customised_design'),
(14,'bouti','bchild'),
(15,'bouti','cpayment'),
(16,'bouti','purchase'),
(17,'bouti','chat'),
(18,'bouti','sizechart'),
(19,'bouti','feedback'),
(20,'bouti','refer_no'),
(21,'bouti','wishlist');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-02-02 17:04:41.550727'),
(2,'auth','0001_initial','2023-02-02 17:04:42.221025'),
(3,'admin','0001_initial','2023-02-02 17:04:42.394499'),
(4,'admin','0002_logentry_remove_auto_add','2023-02-02 17:04:42.419203'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-02-02 17:04:42.440189'),
(6,'contenttypes','0002_remove_content_type_name','2023-02-02 17:04:42.542081'),
(7,'auth','0002_alter_permission_name_max_length','2023-02-02 17:04:42.593700'),
(8,'auth','0003_alter_user_email_max_length','2023-02-02 17:04:42.641445'),
(9,'auth','0004_alter_user_username_opts','2023-02-02 17:04:42.666335'),
(10,'auth','0005_alter_user_last_login_null','2023-02-02 17:04:42.717311'),
(11,'auth','0006_require_contenttypes_0002','2023-02-02 17:04:42.721308'),
(12,'auth','0007_alter_validators_add_error_messages','2023-02-02 17:04:42.738078'),
(13,'auth','0008_alter_user_username_max_length','2023-02-02 17:04:42.788725'),
(14,'auth','0009_alter_user_last_name_max_length','2023-02-02 17:04:42.837654'),
(15,'auth','0010_alter_group_name_max_length','2023-02-02 17:04:42.892975'),
(16,'auth','0011_update_proxy_permissions','2023-02-02 17:04:42.921717'),
(17,'auth','0012_alter_user_first_name_max_length','2023-02-02 17:04:42.977677'),
(18,'bouti','0001_initial','2023-02-02 17:04:43.563872'),
(19,'sessions','0001_initial','2023-02-02 17:04:43.653002'),
(20,'bouti','0002_cpayment','2023-02-03 04:40:50.406943'),
(21,'bouti','0003_chat_purchase','2023-02-03 13:34:30.403410'),
(22,'bouti','0004_sizechart','2023-02-17 04:08:17.519552'),
(23,'bouti','0005_feedback','2023-02-17 13:57:18.469251'),
(24,'bouti','0006_remove_design_sizes','2023-02-18 03:22:28.839823'),
(25,'bouti','0007_refer_no','2023-02-18 05:54:40.464743');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('sfvmcxfkatgidm87b2i28rb5pbgbfu10','eyJsb2dpbl9pZCI6MX0:1pNxGB:v49h5PedmA-h_M8WRM_8FohgSoCB5iyerONu9PihYtc','2023-02-17 14:41:51.529281'),
('eszhdwx022cjr2mdcolcbws52k9fxgv9','eyJsb2dpbl9pZCI6NH0:1pO0Kk:-z2xt9Fs45lOccnm6stljW6oYJfhmua6uk35b74SiAY','2023-02-17 17:58:46.570956'),
('7te60dhihw4nusv8lejobr8u1u03256x','eyJsb2dpbl9pZCI6MX0:1pTJSA:t31K2M8EOf0zFV5ofZMglhWqUR4W3GNyOJG3mxow_I8','2023-03-04 09:24:22.158458'),
('kzvacdta3zlunyfwryyb9jxlcro0ps4x','eyJsb2dpbl9pZCI6M30:1pTHvS:Wd1AfdzBxAfPLS0FMOikpMdNHnQVxDaaARUcdx6Vdpk','2023-03-04 07:46:30.398748'),
('4heig1v2kmsm71y1nu67tadj5rdw73ut','eyJsb2dpbl9pZCI6MX0:1pU1Nb:i1rLE_DvZ9fD99o2lluyMAAKlAwbSUT_Rx0K_KxlkKY','2023-03-06 08:18:35.316438'),
('pekxucvonsezenwt64umv3xp6jwg5kok','eyJsb2dpbl9pZCI6NH0:1pYB3c:Mb-a_h-lUcidejtKMPJWy0xsJOJE6HjWW8iaXf5s7Co','2023-03-17 19:27:08.068685'),
('egpvnkcy6bnqomxjdfpxzicnownook2x','eyJsb2dpbl9pZCI6NH0:1pYMxF:hRUun5x_2ju7ZCWX607ao45FD0g29f75FI2gS_hqFcs','2023-03-18 08:09:21.111535'),
('71rmfie1lpxuqjcdn6kbmxs844ctj40y','eyJsb2dpbl9pZCI6MX0:1pYMyo:mmg2iUHLMiAC7-ICtZ501Bl7GHBx9GVDVTn0DYFRDoM','2023-03-18 08:10:58.256322');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
