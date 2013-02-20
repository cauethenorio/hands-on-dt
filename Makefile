NO_COLOR	= \033[0m
BLUE_COLOR 	= \033[34;01m
GREEN_COLOR	= \033[32;01m

START_PREFIX	= $(BLUE_COLOR)\xe2\x97\x86 $(NO_COLOR)
DONE_PREFIX	= $(GREEN_COLOR)\xe2\x9c\x93 $(NO_COLOR)

NAME=
STATIC_DIR=			{{ project_name }}/assets/static
REDACTOR_DIR=		${STATIC_DIR}/components/redactor

.PHONY: redactor assets settings name messages compilemessages

redactor:
ifeq ($(wildcard ${REDACTOR_DIR}),)
	@mkdir -p ${STATIC_DIR}/{css,/components}
	@if test -d ${REDACTOR_DIR}; then rm -r ${REDACTOR_DIR}; fi
	@echo "${START_PREFIX}Downloading Redactor..."
	@curl --location -o redactor.zip http://imperavi.com/webdownload/redactor/getold/
	@curl --location -o pt_br.js http://imperavi.com/webdownload/redactor/lang/?lang=pt_br
	@unzip -q redactor.zip -d redactor
	@mv -f redactor/redactor ${STATIC_DIR}/components
	@mv -f pt_br.js ${REDACTOR_DIR}
	@rm -Rf redactor{,.zip}
	@echo "${DONE_PREFIX}Redactor installed\n"
else
	@echo "${DONE_PREFIX}Redactor is already installed."
	@echo "  To reinstall remove the '${REDACTOR_DIR}' directory\n"
endif

assets: redactor
	@echo "${START_PREFIX}Installing bower components..."
	@cd ${STATIC_DIR} ; bower install
	@echo "Bower components installed"
	@echo "${DONE_PREFIX}Assets done\n"

settings:
	@echo "${START_PREFIX}Creating environment.py settings file from template..."
	@cp {{ project_name }}/settings/environment.py.template {{ project_name }}/settings/environment.py
	@echo "Generating session and HMAC private keys..."
	@sed -i.bkp -e "s/__YYYY-MM-DD__/`date "+%Y-%m-%d"`/g" {{ project_name }}/settings/environment.py
	@sed -i.bkp -e "s/__secret_key__/`base64 /dev/urandom | tr -d '+/\r\n' | head -c 50`/g" {{ project_name }}/settings/environment.py
	@sed -i.bkp -e "s/__secret_key_2__/`base64 /dev/urandom | tr -d '+/\r\n\\' | head -c 50`/g" {{ project_name }}/settings/environment.py
	@echo "${DONE_PREFIX}Settings done\n"

name:
ifeq ($(NAME),)
	@echo Usage: make name NAME=\"Project name\"
else
	@echo "${START_PREFIX}Changing project name in templates..."
	@find . -name '*.jade' -or -name '*.py' -exec sed -i -e 's/__project_name__/$(NAME)/g' {} \;
	@find . -name '*.jade-e' -or -name '*.py-e' -exec rm {} \;
	@echo "${DONE_PREFIX}Project name updated in jade templates\n"
endif

messages:
	@echo "${START_PREFIX}Collecting en i18n messages..."
	@cd {{ project_name }} ; ../manage.py makemessages -v 1 -l en -e jade,html,txt

compilemessages:
	@echo "${START_PREFIX}Compiling i18n messages..."
	@cd {{ project_name }} ; ../manage.py compilemessages