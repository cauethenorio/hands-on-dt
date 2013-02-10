NAME=
STATIC_DIR={{ project_name }}/assets/static

.PHONY: bootstrap assets settings name

bootstrap:
	@mkdir -p ${STATIC_DIR}/css ${STATIC_DIR}/js/components
	@-test -d ${STATIC_DIR}/css/bootstrap && rm -r ${STATIC_DIR}/css/bootstrap
	@echo "Downloading Bootstrap..."
	@curl --location -o bootstrap.zip http://twitter.github.com/bootstrap/assets/bootstrap.zip
	@unzip bootstrap.zip
	@mv bootstrap/css ${STATIC_DIR}/css/bootstrap
	@mv bootstrap/img ${STATIC_DIR}/css
	@mv bootstrap/js ${STATIC_DIR}/js/components/bootstrap
	@rm -Rf bootstrap bootstrap.zip
	@echo "Bootstrap installed"

assets: bootstrap
	@echo "Installing bower components..."
	@cd ${STATIC_DIR}/js ; bower install
	@echo "Bower components installed"
	@echo "Assets done"

settings:
	@echo "Creating environment.py settings file from template..."
	@cp {{ project_name }}/settings/environment.py.template {{ project_name }}/settings/environment.py
	@echo "Generating session and HMAC private keys..."
	@sed -i.bkp -e "s/__YYYY-MM-DD__/`date "+%Y-%m-%d"`/g" {{ project_name }}/settings/environment.py
	@sed -i.bkp -e "s/__secret_key__/`base64 /dev/urandom | tr -d '+/\r\n' | head -c 50`/g" {{ project_name }}/settings/environment.py
	@sed -i.bkp -e "s/__secret_key_2__/`base64 /dev/urandom | tr -d '+/\r\n\\' | head -c 50`/g" {{ project_name }}/settings/environment.py
	@echo "Settings done"

name:
ifeq ($(NAME),)
	@echo Usage: make name NAME=\"Project name\"
else
	@echo "Changing project name in templates..."
	@find . -name *.jade -exec sed -i -e 's/__project_name__/$(NAME)/g' {} \;
	@find . -name *.jade-e -exec rm {} \;
	@echo "Project name updated in jade templates"
endif
