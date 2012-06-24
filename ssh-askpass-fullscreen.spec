Summary:	SSH X11 passphrase dialog
Summary(de):	SSH X11 Passwort-Dialog
Summary(es):	Di�logo para introducci�n de passphrase para X11
Summary(fr):	Dialogue pass-phrase X11 d'SSH
Summary(it):	Finestra di dialogo X11 per la frase segreta di SSH
Summary(pl):	Odpytywacz has�a SSH dla X11
Summary(pt):	Di�logo de pedido de senha para X11 do SSH
Summary(pt_BR):	Di�logo para entrada de passphrase para X11
Summary(ru):	SSH - ������ ����� �������� ����� (passphrase) ��� X11
Summary(uk):	SSH - Ħ���� ����� ������ϧ ����� (passphrase) ��� X11
Name:		ssh-askpass-fullscreen
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://ftp.debian.org/debian/pool/main/s/ssh-askpass-fullscreen/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c46ad80b6bb150270514317001a2cedc
BuildRequires:	gtk+2-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
This is an X11-based passphrase dialog for use with SSH.

%description -l es
Este paquete contiene un programa que abre una caja de di�logo para
entrada de passphrase en X11.

%description -l pl
To jest bazuj�cy na X11 odpytywacz has�a do u�ytku z SSH.

%description -l pt_BR
Esse pacote cont�m um programa que abre uma caixa de di�logo para
entrada de passphrase no X11.

%description -l ru
Ssh (Secure Shell) - ��� ��������� ��� "������" (login) �� ���������
������ � ��� ���������� ������ �� ��������� ������.

���� ����� �������� ������ ����� �������� ����� ��� ������������� ���
X11.

%description -l uk
Ssh (Secure Shell) - �� �������� ��� "������" (login) �� צ������ϧ
������ �� ��� ��������� ������ �� צ�����Φ� ����Φ.

��� ����� ͦ����� Ħ���� ����� ������ϧ ����� ��� ������������ Ц�
X11.

%prep
%setup -q

%build
%{__cc} gtk2-ssh-askpass.c \
	%{rpmcflags} -Wall \
	-o gtk2-ssh-askpass \
	`pkg-config --libs gtk+-2.0` \
	`pkg-config --cflags gtk+-2.0`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libexecdir}/ssh

install gtk2-ssh-askpass $RPM_BUILD_ROOT%{_libexecdir}/ssh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/ssh/*
