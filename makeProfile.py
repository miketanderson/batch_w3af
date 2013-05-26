
targetURL = "http://www.website.com/junk.php"
outputPath = "/data/apps/w3af/output/"
cookieFile = "/data/apps/w3af/cookies.txt"
localIP = "192.168.1.180"
profName = "BatchScan"


profile = "\n"
profile += "[profile]" + "\n"
profile += "description = Custom Profile For Batch Scanning" + "\n"
profile += "name = " + profName + "\n"
profile += "" + "\n"
profile += "[audit.xpath]" + "\n"
profile += "" + "\n"
profile += "[audit.file_upload]" + "\n"
profile += "" + "\n"
profile += "[audit.sqli]" + "\n"
profile += "" + "\n"
profile += "[audit.xst]" + "\n"
profile += "" + "\n"
profile += "[audit.cors_origin]" + "\n"
profile += "" + "\n"
profile += "[audit.generic]" + "\n"
profile += "diff_ratio = 0.3" + "\n"
profile += "" + "\n"
profile += "[audit.os_commanding]" + "\n"
profile += "" + "\n"
profile += "[audit.format_string]" + "\n"
profile += "" + "\n"
profile += "[audit.lfi]" + "\n"
profile += "" + "\n"
profile += "[audit.blind_sqli]" + "\n"
profile += "" + "\n"
profile += "[audit.mx_injection]" + "\n"
profile += "" + "\n"
profile += "[audit.ssi]" + "\n"
profile += "" + "\n"
profile += "[audit.ldapi]" + "\n"
profile += "" + "\n"
profile += "[audit.eval]" + "\n"
profile += "" + "\n"
profile += "[audit.xss]" + "\n"
profile += "" + "\n"
profile += "[audit.buffer_overflow]" + "\n"
profile += "" + "\n"
profile += "[audit.rfi]" + "\n"
profile += "" + "\n"
profile += "[audit.preg_replace]" + "\n"
profile += "" + "\n"
profile += "[grep.dom_xss]" + "\n"
profile += "" + "\n"
profile += "[grep.code_disclosure]" + "\n"
profile += "" + "\n"
profile += "[grep.error_500]" + "\n"
profile += "" + "\n"
profile += "[output.html_file]" + "\n"
profile += "output_file = " + outputPath + "report.html" + "\n"
profile += "verbose = False" + "\n"
profile += "" + "\n"
profile += "[output.text_file]" + "\n"
profile += "verbose = True" + "\n"
profile += "output_file = " + outputPath + "output.txt" + "\n"
profile += "http_output_file = " + outputPath + "w3af_http.txt" + "\n"
profile += "" + "\n"
profile += "[output.console]" + "\n"
profile += "verbose = False" + "\n"
profile += "" + "\n"
profile += "[target]" + "\n"
profile += "target = " + targetURL + "\n"
profile += "" + "\n"
profile += "[misc-settings]" + "\n"
profile += "fuzz_cookies = False" + "\n"
profile += "fuzz_form_files = True" + "\n"
profile += "fuzz_url_filenames = False" + "\n"
profile += "fuzz_url_parts = False" + "\n"
profile += "fuzzed_files_extension = gif" + "\n"
profile += "fuzzable_headers = " + "\n"
profile += "form_fuzzing_mode = tmb" + "\n"
profile += "stop_on_first_exception = False" + "\n"
profile += "max_discovery_time = 120" + "\n"
profile += "interface = wlan0" + "\n"
profile += "local_ip_address = " + localIP + "\n"
profile += "non_targets = " + "\n"
profile += "msf_location = /opt/metasploit3/bin/" + "\n"
profile += "" + "\n"
profile += "[http-settings]" + "\n"
profile += "timeout = 15" + "\n"
profile += "headers_file = " + "\n"
profile += "basic_auth_user = " + "\n"
profile += "basic_auth_passwd = " + "\n"
profile += "basic_auth_domain = " + "\n"
profile += "ntlm_auth_domain = " + "\n"
profile += "ntlm_auth_user = " + "\n"
profile += "ntlm_auth_passwd = " + "\n"
profile += "ntlm_auth_url = " + "\n"
profile += "cookie_jar_file = " + cookieFile + "\n"
profile += "ignore_session_cookies = False" + "\n"
profile += "proxy_port = 8080" + "\n"
profile += "user_agent = w3af.org" + "\n"
profile += "max_file_size = 400000" + "\n"
profile += "max_http_retries = 2" + "\n"
profile += "always_404 = " + "\n"
profile += "never_404 = " + "\n"
profile += "string_match_404 = " + "\n"
profile += "url_parameter = " + "\n"
profile += "\n"


profFile = open(profName + ".pw3af","w")
profFile.write(profile)
profFile.close()
