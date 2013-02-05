STATIC_DIR={{ project_name }}/assets/static

.PHONY: bootstrap assets settings

bootstrap:
	mkdir -p ${STATIC_DIR}/css ${STATIC_DIR}/js/components
	-test -d ${STATIC_DIR}/css/bootstrap && rm -r ${STATIC_DIR}/css/bootstrap
	curl --location -o bootstrap.zip http://twitter.github.com/bootstrap/assets/bootstrap.zip
	unzip bootstrap.zip
	mv bootstrap/css ${STATIC_DIR}/css/bootstrap
	mv bootstrap/img ${STATIC_DIR}/css
	mv bootstrap/js ${STATIC_DIR}/js/components/bootstrap
	rm -Rf bootstrap bootstrap.zip

assets: bootstrap
	echo ${STATIC_DIR}
	cd ${STATIC_DIR}/js ; bower install

settings:
	echo ${DATE}
	cp {{ project_name }}/settings/environment.py.template {{ project_name }}/settings/environment.py
	sed -i.bkp -e "s/__YYYY-MM-DD__/`date "+%Y-%m-%d"`/g" {{ project_name }}/settings/environment.py
	sed -i.bkp -e "s/__secret_key__/`base64 /dev/urandom | tr -d '+/\r\n' | head -c 50`/g" {{ project_name }}/settings/environment.py
	sed -i.bkp -e "s/__secret_key_2__/`base64 /dev/urandom | tr -d '+/\r\n\\' | head -c 50`/g" {{ project_name }}/settings/environment.py