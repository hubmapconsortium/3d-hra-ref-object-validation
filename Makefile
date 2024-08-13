REF_ORGAN_URL = https://github.com/hubmapconsortium/hra-ref-organ-validation/raw/main/data/ref-organ-relations.csv

tests/ref-organ-relations-full.csv:
	curl -L $(REF_ORGAN_URL) -o $@

split_files: tests/ref-organ-relations-full.csv
	python src/split_results.py

validation-config.yml: split_files
	cat validation-config-properties.yml output.yaml > $@
	rm output.yaml


.PHONY: reports
reports: validation-config.yml
	python src/validation.py --config validation-config.yml

