#
#
%define name_dash tty_ctrl
Summary:	-
Summary(pl):	-
Name:		ttyctrl
Version:	2_00
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
#Vendor:		-
Group:		Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/ttyctrl/tty_ctrl_%{version}.tgz
# Source0-md5:	7ba345323d89833b18a4fbb47f6086ff
Patch0:		%{name}-makefile.patch
URL:		http://ttyctrl.sourceforge.net
#Obsoletes:	cpanel
#from http://www.linux-magazin.de/ausgabe/2000/09/Seriell/seriell.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When running a server on linux without keyboard, mouse and monitor, it
is sometimes necessary to excute administrative commands. Tty_ctrl
offer's the opportunity to execute 7 sommands on such a computer.
Success or Errors while execution of the commands will be displayed
via status led's. You'll need a free serial line, three resistors, 7
buttons, three led's 6 diodes and of course a soldering pen to get
this stuff together.

%description -l pl
Gdy u¿ywasz serwera linuksowego bez klawiatury, myszki i monitora,
czasem zachodzi potrzeba wydania poleceñ administracyjnych. Tty_ctrl
oferuje mo¿liwo¶æ wykonania 7 komend na takim komputerze. Wyniki
wykonania poleceñ s± sygnalizowane diodami LED. Bêdziesz potrzebowa³
nie zajêtego portu szeregowego, trzech oporników, siedmiu przycisków,
3 LED, 6 diód i lutownicy aby to po³±czyæ.

%prep
%setup -q -n %{name_dash}_%{version}
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{ttyctrl,rc.d/init.d},/sbin,%{_examplesdir}/%{name}}

install tty_control		$RPM_BUILD_ROOT/sbin
install %{name_dash}	$RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install etc_tty_ctrl/*	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# XXX don't touch my hardware by default unitl I SAY SO:
#  /etc/rc.d/init.d/%{name_dash} start 
# XXX

%preun
if [ "$1" = "0" ]; then
   /etc/rc.d/init.d/%{name_dash} stop
   /sbin/chkconfig --del %{name}
fi


%files
%defattr(644,root,root,755)
%doc info.txt      readme 

%attr(755,root,root) /sbin/*

%{_examplesdir}/%{name}

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/ttyctrl

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name_dash}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name_dash}
