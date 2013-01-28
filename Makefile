STATIC_DIR={{ project_name }}/assets/static

.PHONY: bootstrap assets

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
	cd ${STATIC_DIR}/js
	bower install