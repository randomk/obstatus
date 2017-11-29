# Set some constants
username='<>'
password='<>'

import os
import socket
localhost = socket.gethostname()
url = 't3:' + localhost + ':7001'
print url


print "Statistics Proxy & Business services "

connect(username, password,url)


from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.config import Ref
from java.lang import String
from com.bea.wli.config import Ref
from com.bea.wli.sb.util import Refs
from com.bea.wli.sb.management.configuration import CommonServiceConfigurationMBean
from com.bea.wli.sb.management.configuration import SessionManagementMBean
from com.bea.wli.sb.management.configuration import ALSBConfigurationMBean
from com.bea.wli.sb.management.configuration import ProxyServiceConfigurationMBean
from com.bea.wli.monitoring import StatisticType
from com.bea.wli.monitoring import ServiceDomainMBean
from com.bea.wli.monitoring import ServiceResourceStatistic
from com.bea.wli.monitoring import StatisticValue
from com.bea.wli.monitoring import ResourceType



domainRuntime()


    # obtain the ALSBConfigurationMBean instance that operates
    # on the session that has just been created. Notice that
    # the name of the mbean contains the session name.
alsbCore = findService(ALSBConfigurationMBean.NAME, ALSBConfigurationMBean.TYPE)
refs = alsbCore.getRefs(Ref.DOMAIN)
it = refs.iterator()
while it.hasNext():
    r = it.next()
    if r.getTypeId() == Ref.PROJECT_REF:
        print "Project Name : " + (r.getProjectName())
        allRefs= alsbCore.getRefs(Ref.DOMAIN)
# Now you can get a list of all of the objects within the domain by name
# and step through them one by one
        for ref in refs:
   #   Identify the proxy service references
          typeId = ref.getTypeId()
          if typeId == "ProxyService":
      # and listing them
             print "Proxy Service: " + '\033[1;32m' + ref.getFullName() + '\033[0m'
             print "------------------------------------"
             cd('domainRuntime:/DomainServices/ServiceDomain')
             stats = cmo.getProxyServiceStatistics([ref],ResourceType.SERVICE.value(),'')
             for ps in stats[ref].getAllResourceStatistics():
                 for s in ps.getStatistics():
                         if s.getType() == StatisticType.COUNT:
                             print s.getName() + "("+ str(s.getType()) +"): " + str(s.getCount())
                         if s.getType() == StatisticType.INTERVAL:
                             print ( s.getName() + "("+ str(s.getType()) +"): " + str(s.getMin()) + " " + str(s.getMax()) + " " + str(s.getAverage()) + " " + str(s.getSum())
                         if s.getType() == StatisticType.STATUS:
                             print s.getName() + "("+ str(s.getType()) +"): " + str(s.getCurrentStatus()) + "(" + str(s.getInitialStatus()) + ")"


disconnect()
exit()
