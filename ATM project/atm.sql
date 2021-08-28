-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2019 at 02:03 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atm`
--

-- --------------------------------------------------------

--
-- Table structure for table `alogin`
--

CREATE TABLE `alogin` (
  `id` int(11) NOT NULL,
  `password` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alogin`
--

INSERT INTO `alogin` (`id`, `password`) VALUES
(101, 'admin@101');

-- --------------------------------------------------------

--
-- Table structure for table `hdfc`
--

CREATE TABLE `hdfc` (
  `account` bigint(20) NOT NULL,
  `amount` bigint(20) DEFAULT NULL,
  `ifsc` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hdfc`
--

INSERT INTO `hdfc` (`account`, `amount`, `ifsc`) VALUES
(2220002456, 5500, 'hdfc2456');

-- --------------------------------------------------------

--
-- Table structure for table `mini`
--

CREATE TABLE `mini` (
  `account` bigint(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `withd` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `dep` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mini`
--

INSERT INTO `mini` (`account`, `pin`, `withd`, `time`, `dep`) VALUES
(111001234, 2214, 67, '2019-05-17 18:05:01', NULL),
(111001234, 2214, 200, '2019-05-18 11:05:24', NULL),
(111001234, 1996, 500, '2019-05-18 16:34:00', NULL),
(111001234, 1996, NULL, '2019-05-18 16:35:17', 200),
(111001234, 1996, 500, '2019-05-18 16:45:49', NULL),
(111001234, 1996, 400, '2019-05-18 17:06:48', NULL),
(111001234, 1996, 500, '2019-05-18 17:09:09', NULL),
(111001567, 6732, NULL, '2019-05-18 17:17:13', 500),
(111001567, 6732, 200, '2019-05-18 17:18:03', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pnb`
--

CREATE TABLE `pnb` (
  `account` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pnb`
--

INSERT INTO `pnb` (`account`, `name`, `amount`, `address`, `contact`, `pin`) VALUES
(111001234, 'puja', 3077, 'delhi', 8629053320, 1996),
(111001567, 'simar', 3344, 'amritsar', 9910634341, 6732);

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `account` bigint(20) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `ifsc` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`account`, `amount`, `ifsc`) VALUES
(111000111345, 55000, 'sb345');

-- --------------------------------------------------------

--
-- Table structure for table `ulogin`
--

CREATE TABLE `ulogin` (
  `id` int(11) NOT NULL,
  `password` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alogin`
--
ALTER TABLE `alogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hdfc`
--
ALTER TABLE `hdfc`
  ADD PRIMARY KEY (`account`);

--
-- Indexes for table `pnb`
--
ALTER TABLE `pnb`
  ADD PRIMARY KEY (`account`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`account`);

--
-- Indexes for table `ulogin`
--
ALTER TABLE `ulogin`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
