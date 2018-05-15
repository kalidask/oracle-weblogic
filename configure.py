domain_name  = os.environ.get("DOMAIN_NAME")  
domain_home  = os.environ.get("DOMAIN_HOME")  
print('domain_name : [%s]' % domain_name);
print('domain_home : [%s]' % domain_home);

readTemplate("/u01/oracle/wlserver/common/templates/wls/wls.jar")  
set('Name', domain_name)  
cd('/Servers/AdminServer')  
cd('/Security/%s/User/weblogic' % domain_name)  
cmo.setPassword('temporarypass')  
setOption('OverwriteDomain', 'true')  
setOption('ServerStartMode', 'prod')  
writeDomain(os.environ.get("DOMAIN_HOME"))  
closeTemplate()  
exit()  
