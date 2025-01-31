 
APP_SRC_DIR = $$PWD/../../../../src/

INCLUDEPATH += $$APP_SRC_DIR

HEADERS  += \
    $$PWD/test_*.h \
    $$APP_SRC_DIR/version.h \
    $$APP_SRC_DIR/release.h \
    $$APP_SRC_DIR/services/databaseservice.h \
    $$APP_SRC_DIR/libraries/piwiktracker/piwiktracker.h \
    $$APP_SRC_DIR/services/metricsservice.h \
    $$APP_SRC_DIR/services/cryptoservice.h \
    $$APP_SRC_DIR/entities/note.h \
    $$APP_SRC_DIR/entities/calendaritem.h \
    $$APP_SRC_DIR/helpers/htmlentities.h \
    $$APP_SRC_DIR/helpers/clientproxy.h \
    $$APP_SRC_DIR/libraries/diff_match_patch/diff_match_patch.h \
    $$APP_SRC_DIR/libraries/hoedown/*.h \
    $$APP_SRC_DIR/libraries/simplecrypt/simplecrypt.h \
    $$APP_SRC_DIR/libraries/botan/botanwrapper.h \
    $$APP_SRC_DIR/libraries/qmarkdowntextedit/lib/peg-markdown-highlight/pmh_definitions.h \
    $$APP_SRC_DIR/libraries/qmarkdowntextedit/lib/peg-markdown-highlight/pmh_parser.h \
    $$APP_SRC_DIR/libraries/qmarkdowntextedit/highlighter.h

SOURCES += \
    $$PWD/test_*.cpp \
    $$APP_SRC_DIR/services/databaseservice.cpp \
    $$APP_SRC_DIR/libraries/piwiktracker/piwiktracker.cpp \
    $$APP_SRC_DIR/services/metricsservice.cpp \
    $$APP_SRC_DIR/services/cryptoservice.cpp \
    $$APP_SRC_DIR/entities/note.cpp \
    $$APP_SRC_DIR/entities/calendaritem.cpp \
    $$APP_SRC_DIR/helpers/htmlentities.cpp \
    $$APP_SRC_DIR/helpers/clientproxy.cpp \
    $$APP_SRC_DIR/libraries/diff_match_patch/diff_match_patch.cpp \
    $$APP_SRC_DIR/libraries/hoedown/*.c \
    $$APP_SRC_DIR/libraries/simplecrypt/simplecrypt.cpp \
    $$APP_SRC_DIR/libraries/botan/botanwrapper.cpp \
    $$APP_SRC_DIR/libraries/qmarkdowntextedit/lib/peg-markdown-highlight/pmh_parser.c \
    $$APP_SRC_DIR/libraries/qmarkdowntextedit/highlighter.cpp

include($$APP_SRC_DIR/libraries/botan/botan.pri)

#OTHER_FILES += \
#    connections.xml

#FORMS += \
#    $$APP_SRC_DIR/forms/connection.ui \
