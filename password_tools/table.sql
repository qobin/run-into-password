-- ----------------------------
-- 密码集中营
-- ----------------------------
DROP TABLE IF EXISTS `camp`;
CREATE TABLE `camp` (
`id` bigint(11) not null auto_increment comment '主键',
`password` varchar(20) NOT NULL COMMENT '明文密码',
`password_md5` varchar(32) DEFAULT NULL COMMENT 'MD5加密密码',
PRIMARY KEY (`id`),
index MD5_INX(`password_md5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='密码集中营';