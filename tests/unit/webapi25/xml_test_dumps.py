#!/usr/bin/env python

"""XML dumps for PyOWM test objects"""

LOCATION_XML_DUMP = """<?xml version='1.0' encoding='utf8'?>
<location xmlns:l="http://github.com/csparpa/pyowm/tree/master/pyowm/webapi25/xsd/location.xsd"><l:name>London</l:name><l:coordinates><l:lon>12.3</l:lon><l:lat>43.7</l:lat></l:coordinates><l:ID>1234</l:ID><l:country>UK</l:country></location>"""

WEATHER_XML_DUMP = """<?xml version='1.0' encoding='utf8'?>
<weather xmlns:w="http://github.com/csparpa/pyowm/tree/master/pyowm/webapi25/xsd/weather.xsd"><w:status>Clouds</w:status><w:weather_code>804</w:weather_code><w:rain><w:all>20</w:all></w:rain><w:snow><w:all>0</w:all></w:snow><w:pressure><w:press>1030.119</w:press><w:sea_level>1038.589</w:sea_level></w:pressure><w:sunrise_time>1378449600</w:sunrise_time><w:weather_icon_name>04d</w:weather_icon_name><w:clouds>67</w:clouds><w:temperature><w:temp_kf>-1.899</w:temp_kf><w:temp_min>294.199</w:temp_min><w:temp>294.199</w:temp><w:temp_max>296.098</w:temp_max></w:temperature><w:detailed_status>Overcast clouds</w:detailed_status><w:reference_time>1378459200</w:reference_time><w:sunset_time>1378496400</w:sunset_time><w:humidity>57</w:humidity><w:wind><w:speed>1.1</w:speed><w:deg>252.002</w:deg></w:wind></weather>"""

OBSERVATION_XML_DUMP = """<?xml version='1.0' encoding='utf8'?>
<observation xmlns:o="http://github.com/csparpa/pyowm/tree/master/pyowm/webapi25/xsd/observation.xsd"><o:reception_time>1234567</o:reception_time><o:location><o:name>test</o:name><o:coordinates><o:lon>12.3</o:lon><o:lat>43.7</o:lat></o:coordinates><o:ID>987</o:ID><o:country>UK</o:country></o:location><o:weather><o:status>Clouds</o:status><o:weather_code>804</o:weather_code><o:rain><o:all>20</o:all></o:rain><o:snow><o:all>0</o:all></o:snow><o:pressure><o:press>1030.119</o:press><o:sea_level>1038.589</o:sea_level></o:pressure><o:sunrise_time>1378449600</o:sunrise_time><o:weather_icon_name>04d</o:weather_icon_name><o:clouds>67</o:clouds><o:temperature><o:temp_kf>-1.899</o:temp_kf><o:temp_min>294.199</o:temp_min><o:temp>294.199</o:temp><o:temp_max>296.098</o:temp_max></o:temperature><o:detailed_status>Overcast clouds</o:detailed_status><o:reference_time>1378459200</o:reference_time><o:sunset_time>1378496400</o:sunset_time><o:humidity>57</o:humidity><o:wind><o:speed>1.1</o:speed><o:deg>252.002</o:deg></o:wind></o:weather></observation>"""

FORECAST_XML_DUMP = """<?xml version='1.0' encoding='utf8'?>
<forecast xmlns:f="http://github.com/csparpa/pyowm/tree/master/pyowm/webapi25/xsd/forecast.xsd"><f:interval>daily</f:interval><f:reception_time>1234567</f:reception_time><f:location><f:name>test</f:name><f:coordinates><f:lon>12.3</f:lon><f:lat>43.7</f:lat></f:coordinates><f:ID>987</f:ID><f:country>IT</f:country></f:location><f:weathers><f:weather><f:status>Clouds</f:status><f:weather_code>804</f:weather_code><f:rain><f:all>20</f:all></f:rain><f:snow><f:all>0</f:all></f:snow><f:pressure><f:press>1030.119</f:press><f:sea_level>1038.589</f:sea_level></f:pressure><f:sunrise_time>1378449600</f:sunrise_time><f:weather_icon_name>04d</f:weather_icon_name><f:clouds>67</f:clouds><f:temperature><f:temp_kf>-1.899</f:temp_kf><f:temp_min>294.199</f:temp_min><f:temp>294.199</f:temp><f:temp_max>296.098</f:temp_max></f:temperature><f:detailed_status>Overcast clouds</f:detailed_status><f:reference_time>1378459200</f:reference_time><f:sunset_time>1378496400</f:sunset_time><f:humidity>57</f:humidity><f:wind><f:speed>1.1</f:speed><f:deg>252.002</f:deg></f:wind></f:weather><f:weather><f:status>Clear</f:status><f:weather_code>804</f:weather_code><f:rain><f:all>10</f:all></f:rain><f:snow><f:all>0</f:all></f:snow><f:pressure><f:press>1070.119</f:press><f:sea_level>1078.589</f:sea_level></f:pressure><f:sunrise_time>1378449510</f:sunrise_time><f:weather_icon_name>02d</f:weather_icon_name><f:clouds>23</f:clouds><f:temperature><f:temp_kf>-1.899</f:temp_kf><f:temp_min>295.6</f:temp_min><f:temp>297.199</f:temp><f:temp_max>299.0</f:temp_max></f:temperature><f:detailed_status>Sky is clear</f:detailed_status><f:reference_time>1378459690</f:reference_time><f:sunset_time>1378496480</f:sunset_time><f:humidity>12</f:humidity><f:wind><f:speed>4.2</f:speed><f:deg>103.4</f:deg></f:wind></f:weather></f:weathers></forecast>"""

STATIONHISTORY_XML_DUMP = """<?xml version='1.0' encoding='utf8'?>
<station_history xmlns:sh="http://github.com/csparpa/pyowm/tree/master/pyowm/webapi25/xsd/station_history.xsd"><sh:station_id>2865</sh:station_id><sh:interval>tick</sh:interval><sh:reception_time>1378684800</sh:reception_time><sh:measurements><sh:measurement><sh:temperature>266.85</sh:temperature><sh:reference_time>1362934043</sh:reference_time><sh:humidity>27.7</sh:humidity><sh:pressure>1010.09</sh:pressure><sh:wind>4.7</sh:wind></sh:measurement><sh:measurement><sh:temperature>266.25</sh:temperature><sh:reference_time>1362933983</sh:reference_time><sh:humidity>27.3</sh:humidity><sh:pressure>1010.02</sh:pressure><sh:wind>4.7</sh:wind></sh:measurement></sh:measurements></station_history>"""
