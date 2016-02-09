require 'net/ssh'
require 'json'
require_relative 'configuration'

class CliAccess < Fetcher

  @@initialized  = false
  
  def initialize()
    @@initialized && return
    @@config = Configuration.instance.get('CLI')
    @host = @@config['host']
    @user = @@config['user']
    @key = @@config['keyfile']
    @pwd = @@config['pwd']
    if (@host == nil or @user == nil or (@key == nil) && (@pwd == nil))
      raise ArgumentError, 'Missing definition of host, user or key/pwd for CLI access'
    end
  end
 
  def run(cmd)
    Net::SSH.start(
        @host, @user,
        :auth_methods => ['password'],
        #:keys => [ @key ]
        :password => @pwd
    ) do |ssh|
      result = ssh.exec!("cmd")
      return result
    end
  end
  
end