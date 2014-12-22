INCLUDES = -I$(top_srcdir)/src/libipulog/include

sbin_PROGRAMS = fprobe-ulog
fprobe_ulog_SOURCES = fprobe-ulog.c fprobe-ulog.h \
	netflow.c netflow.h \
	hash.c hash.h \
	mem.c mem.h \
	my_getopt.c my_getopt.h \
	my_log.c my_log.h \
	common.h my_inttypes.h

man_MANS = fprobe-ulog.8

SUBDIRS = libipulog

EXTRA_DIST = ${man_MANS}

fprobe_ulog_LDADD = libipulog/libipulog.a
