# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$script = <<SCRIPT
echo "---> I am provisioning..."
date > /etc/vagrant_provisioned_at
export DEBIAN_FRONTEND=noninteractive

echo "---> Upgrading system..."
apt-get update || exit 0
apt-get upgrade -q -y || exit 0

echo "---> Installing dependencies..."
apt-get install -q -y \
  postgresql-9.1 postgresql-client-9.1 libpq-dev \
  python-dev python-virtualenv python-pip \
  git mercurial \
  libxml2-dev libxslt-dev || exit 0

echo "---> Setting up virtualenv..."
cd /home/vagrant
sudo -u vagrant virtualenv -q VIRTUAL || exit 0
export DJANGO_DEBUG=True
sudo -u vagrant echo "export DJANGO_DEBUG=True" >> VIRTUAL/bin/activate
export DATABASE_URL='postgres:///pranger'
sudo -u vagrant echo "export DATABASE_URL='postgres:///pranger'" >> VIRTUAL/bin/activate
sudo -u vagrant VIRTUAL/bin/pip install -r pranger/requirements/dev.txt || exit 0

echo "---> Creating database..."
sudo -u postgres createuser -s vagrant || exit 0
sudo -u vagrant createdb pranger || exit 0
sudo -u vagrant -E bash -c "VIRTUAL/bin/python pranger/pranger/manage.py migrate" || exit 0

echo "---> Done!"
echo " "
echo "To start the dev server:"
echo "$ vagrant ssh"
echo "$ . VIRTUAL/bin/activate"
echo "$ cd pranger/pranger"
echo "$ ./manage.py runserver 0.0.0.0:8000"
echo " "

SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "hashicorp/precise32"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/home/vagrant/pranger"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Don't boot with headless mode
  #   vb.gui = true
  #
  #   # Use VBoxManage to customize the VM. For example to change memory:
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
  #
  # View the documentation for the provider you're using for more
  # information on available options.
  
  # Use shell script based provisioning
  config.vm.provision "shell", inline: $script
end
