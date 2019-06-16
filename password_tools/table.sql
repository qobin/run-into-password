-- ----------------------------
-- 密码集中营
-- ----------------------------
DROP TABLE IF EXISTS `camp`;
CREATE TABLE `camp` (
`password` varchar(20) NOT NULL COMMENT '明文密码',
`password_md5` varchar(32) DEFAULT NULL COMMENT 'MD5加密密码',
`password_sha256` varchar(64) default null COMMENT 'SHA256加密密码',
`create_time` datetime default '1970-01-01 08:00:01' COMMENT '创建时间',
PRIMARY KEY (`password`),
index MD5_INX(`password_md5`),
index SHA256_INX(`password_sha256`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='密码集中营';