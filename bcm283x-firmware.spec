#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date	20151212
%global commit_long	36c56b7cab316e657bc00392fd98ceded38a17ae
%global commit_short	%(c=%{commit_long}; echo ${c:0:7})

Name:          bcm283x-firmware
Version:       %{snap_date}
Release:       1.%{commit_short}%{?dist}
Summary:       Broadcom bcm283x firmware for the Raspberry Pi

Group:         System Environment/Kernel
License:       Redistributable, no modification permitted
URL:           https://github.com/raspberrypi/
Source0:       %{name}-%snap_date-%{commit_short}.tar.xz
ExclusiveArch: %{arm}

%description
GPU (VideoCore IV) firmware for the Broadcom bcm283x SoC used in the Raspberry Pi.

%prep
%setup -q -n %{name}-%{commit_short} -c %{name}-%{commit_short}

%build

%install
mkdir -p %{buildroot}/boot
mkdir -p %{buildroot}/boot/overlays
install -p *bin %{buildroot}/boot
install -p *dat %{buildroot}/boot
install -p *elf %{buildroot}/boot
install -p overlays/README %{buildroot}/boot/overlays

%files
%license LICENCE.broadcom
/boot/*


%changelog
* Sat Dec 12 2015 Vaughan <devel at agrez dot net> - 20151212-1.36c56b7
- Sync to latest git commit: 36c56b7cab316e657bc00392fd98ceded38a17ae

* Sun Nov 29 2015 Vaughan <devel at agrez dot net> - 20151125-1.f01ec42
- Sync to latest git commit: f01ec42f66e360a177f82457e3324adbfdf84de5

* Sun Nov 15 2015 Vaughan <devel at agrez dot net> - 20151114-1.fa62739
- Sync to latest git commit: fa627390f76d7d3c38e80fc88ad1cc6697c04334

* Thu Oct 29 2015 Vaughan <devel at agrez dot net> - 20151013-1.4047fe2
- Sync to latest git commit: 4047fe26797884cedf53bc8671d19e7f6f9f59d5

* Tue Oct 13 2015 Vaughan <devel at agrez dot net> - 20151013-1.ba7a8fb
- Sync to latest git revision:
  git commit: ba7a8fb709adab287495f4e836b1cd3e5c9db409

* Thu Sep 24 2015 Vaughan <devel at agrez dot net> - 20150924-1.960832a
- Sync to latest git revision:
  git commit: 960832a6c2590635216c296b6ee0bebf67b21d50

* Thu Sep 17 2015 Vaughan <devel at agrez dot net> - 20150916-1.56d5a7b
- Sync to latest git revision:
  git commit: 56d5a7bca477e0297d94aace43320c38df985015

* Fri Sep 11 2015 Vaughan <devel at agrez dot net> - 20150911-1.fc95251
- Sync to latest git revision:
  git commit: fc952516e1d73d54141861a64ac5d4be17e7a159

* Wed Sep 02 2015 Vaughan <devel at agrez dot net> - 20150902-1.c6ae1d6
- Sync to latest git revision:
  git commit: c6ae1d69860c0915cca303475abc0b4efb83ad08

* Wed Aug 19 2015 Vaughan <devel at agrez dot net> - 20150819-1.b3da683
- Sync to latest git revision:
  git commit: b3da68379785b0e10b09fdaa8db1b6f18732be8e

* Sat Aug 15 2015 Vaughan <devel at agrez dot net> - 20150815-1.c25cc51
- Sync to latest git revision:
  git commit: c25cc51c6fc0ddc4455d56ad26fbbf38b48da33a

* Sat Aug 08 2015 Vaughan <devel at agrez dot net> - 20150808-1.11eaffc
- Update for kernel 4.1.y
  git commit: 11eaffc2bbb61c6911ffa05b80694f9f7d91915c

* Sat Jul 25 2015 Vaughan <devel at agrez dot net> - 20150725-1.464ce4f
- Update for kernel 4.0.9
  git commit: 464ce4fc013ff20a2b957bc47093ed8b557e1ef1

* Sat Jun 27 2015 Vaughan <devel at agrez dot net> - 20150624-1.856e2e1
- Update for kernel 4.0.6
  git commit: 856e2e1907a7f7058289c30268515c8cbf3fa5e3

* Sat Jun 20 2015 Vaughan <devel at agrez dot net> - 20150620-1.8b9d7b8
- Initial build
