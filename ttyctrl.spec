%define name_dash tty_ctrl
Summary:	Executing commands through special serial line device
Summary(pl):	Wykonywanie polece� poprzez specjalne urz�dzenie pod��czone do portu szeregowego
Name:		ttyctrl
Version:	2_00
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/ttyctrl/tty_ctrl_%{version}.tgz
# Source0-md5:	7ba345323d89833b18a4fbb47f6086ff
Patch0:		%{name}-makefile.patch
URL:		http://ttyctrl.sourceforge.net/
#Obsoletes:	cpanel
#from http://www.linux-magazin.de/ausgabe/2000/09/Seriell/seriell.html
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When running a server on Linux without keyboard, mouse and monitor, it
is sometimes necessary to excute administrative commands. Tty_ctrl
offers the opportunity to execute 7 sommands on such a computer.
Success or Errors while execution of the commands will be displayed
via status LEDs. You'll need a free serial line, three resistors, 7
buttons, three LEDs, 6 diodes and of course a soldering pen to get
this stuff together.

%description -l pl
Gdy u�ywamy serwera linuksowego bez klawiatury, myszki i monitora,
czasem zachodzi potrzeba wydania polece� administracyjnych. Tty_ctrl
oferuje mo�liwo�� wykonania 7 polece� na takim komputerze. Wyniki
wykonania polece� s� sygnalizowane diodami LED. Potrzebne s� do tego:
nie zaj�ty port szeregowy, trzy oporniki, siedem przycisk�w, 3 LED-y,
6 diod i oczywi�cie lutownica, aby to wszystko po��czy�.

%prep
%setup -q -n %{name_dash}_%{version}
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,ttyctrl},/sbin,%{_examplesdir}/%{name}-%{version}}

install tty_control	$RPM_BUILD_ROOT/sbin
install %{name_dash}	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install etc_tty_ctrl/*	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}

%preun
if [ "$1" = "0" ]; then
	%service %{name_dash} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc info.txt readme
%attr(755,root,root) /sbin/*
%{_examplesdir}/%{name}-%{version}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ttyctrl
%attr(754,root,root) /etc/rc.d/init.d/%{name_dash}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name_dash}
