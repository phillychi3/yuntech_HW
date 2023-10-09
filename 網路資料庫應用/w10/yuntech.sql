-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 08, 2022 at 07:24 AM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `yuntech`
--

-- --------------------------------------------------------

--
-- Table structure for table `testdb`
--

CREATE TABLE `testdb` (
  `no` int(11) NOT NULL,
  `name` text NOT NULL,
  `Address` text NOT NULL,
  `Tel` text NOT NULL,
  `Birthday` text NOT NULL,
  `Email` text NOT NULL,
  `Proprity` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `testdb`
--

INSERT INTO `testdb` (`no`, `name`, `Address`, `Tel`, `Birthday`, `Email`, `Proprity`) VALUES
(1, '承惠安', '台北某地方', '02-1111111', '1919191919', 'uyguhbjko@ohigvjh.coikj', 'h'),
(2, '將小於', '台北某地方', '02-1111111', '1919191919', 'uyguhbjko@ohigvjh.coikj', 'h'),
(3, '劉德華', '台北某地方', '02-1111111', '1919191919', 'uyguhbjko@ohigvjh.coikj', 'h'),
(4, '黎民', '台北某地方', '02-1111111', '1919191919', 'uyguhbjko@ohigvjh.coikj', 'h');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `testdb`
--
ALTER TABLE `testdb`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `testdb`
--
ALTER TABLE `testdb`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
