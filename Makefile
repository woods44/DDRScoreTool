PYCS	:= $(shell find . -name "*.pyc")
NAME	= DDRScoretool
TARGET	= DDRScoreTool.py
PACKAGE	= ddrscoretool
INSTDIR	= DDRScoretool.app/Contents/Resources/Python/

all:


clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	if [ -e $(INSTDIR) ] ; then rm -f -r $(INSTDIR) ; fi

test:
	python ${TARGET}

install:
	if [ ! -e $(INSTDIR) ] ; then mkdir $(INSTDIR) ; fi
	cp -p -r $(TARGET) $(PACKAGE) $(INSTDIR)

zip: clean
	(cd .. ; zip -r $(NAME).zip ./$(NAME)/)

sdist: clean
	python setup.py sdist

pydoc: clean
	(sleep 3 ; open http://localhost:9999/$(PACKAGE).html) & pydoc -p 9999