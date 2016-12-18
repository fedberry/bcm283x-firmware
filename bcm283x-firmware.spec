#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date       20161218
%global commit_long     2190ebaaab17d690fb4a6aa767ff7755eaf51b12
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name:          bcm283x-firmware
Version:       %{snap_date}
Release:       1.%{commit_short}%{?dist}
Summary:       Broadcom bcm283x firmware for the Raspberry Pi
Group:         System Environment/Kernel
License:       Redistributable, no modification permitted
URL:           https://github.com/raspberrypi/firmware
Source0:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/bootcode.bin
Source1:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/fixup.dat
Source2:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/fixup_cd.dat
Source3:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/fixup_db.dat
Source4:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/fixup_x.dat
Source5:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/start.elf
Source6:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/start_cd.elf
Source7:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/start_db.elf
Source8:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/start_x.elf
Source9:       https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/LICENCE.broadcom
Source10:      https://github.com/raspberrypi/firmware/raw/%{commit_long}/boot/COPYING.linux

ExclusiveArch: %{arm}

%description
GPU (VideoCore IV) firmware for the Broadcom bcm283x SoC used in the Raspberry Pi.

%prep
%setup -c -n %{name}-%{commit_short}
cp -a %{sources} .

%build

%install
mkdir -p %{buildroot}/boot
install -p * %{buildroot}/boot

%files
%license LICENCE.broadcom COPYING.linux
/boot/*


%changelog
* Sun Dec 18 2016 Vaughan <devel at agrez dot net> - 20161218-1.2190eba
- Sync to latest git commit: 2190ebaaab17d690fb4a6aa767ff7755eaf51b12
- Use %{sources} macro in %%prep

* Wed Oct 12 2016 Vaughan <devel at agrez dot net> - 20161012-1.a021d6e
- Sync to latest git commit: a021d6e70bf5a710c364d21852be4a8dd4dc423a

* Wed Oct 05 2016 Vaughan <devel at agrez dot net> - 20161005-1.ec63df1
- Sync to latest git commit: ec63df146f454e8cab7080380f9138246d877013

* Thu Sep 15 2016 Vaughan <devel at agrez dot net> - 20160915-1.83dc067
- Sync to latest git commit: 83dc067c60fd3f66eda1114eab23e45f57be387d
- %%license COPYING.linux

* Mon Aug 15 2016 Vaughan <devel at agrez dot net> - 20160815-1.2cf8fd5
- Sync to latest git commit: 2cf8fd5ba0b195e16627df6a5b45f47c0edc3a54

* Thu Jun 16 2016 Vaughan <devel at agrez dot net> - 20160616-1.fdbca29
- Sync to latest git commit: fdbca29d3863ee16f5eee24c66e826bedf662db5

* Sat Jun 04 2016 Vaughan <devel at agrez dot net> - 20160604-1.70143fe
- Sync to latest git commit: 70143fe9d371cd6486a80d6765e93b5574212b64

* Tue May 24 2016 Vaughan <devel at agrez dot net> - 20160524-1.3b98f74
- Sync to latest git commit: 3b98f7433649e13cf08f54f509d11491c99c4c0b

* Wed Apr 27 2016 Vaughan <devel at agrez dot net> - 20160427-1.20958cd
- Sync to latest git commit: 20958cdfe145aacdc64bded239c9d7bfe1b20bb2

* Sat Mar 19 2016 Vaughan <devel at agrez dot net> - 20160311-1.c230b2b
- Sync to latest git commit: c230b2b9b5a38615a4ab17539c3b438064fe5d83

* Fri Mar 11 2016 Vaughan <devel at agrez dot net> - 20160311-1.8b4e548
- Sync to latest git commit: 8b4e5482b52e6fb438dddc0d88ba0ba8d44af54b

* Mon Mar 07 2016 Vaughan <devel at agrez dot net> - 20160307-1.cb2ffaa
- Don't grab a whole repo snapshot as Source0 is too big (~110 MB).
- Only add the required firmware files / docs as Sources(0-9)
- Drop README file (its provided by the kernel)

* Mon Mar 07 2016 mrjoshuap <jpreston at redhat dot com> - 20160305-1.845eb06
- Sync to latest git commit: 845eb064cb52af00f2ea33c0c9c54136f664a3e4

* Fri Feb 05 2016 Vaughan <devel at agrez dot net> - 20160205-1.cb2ffaa
- Sync to latest git commit: cb2ffaa5503ac53039d40715965480dd66f0aa20

* Wed Dec 23 2015 Vaughan <devel at agrez dot net> - 20151223-1.1efc1ec
- Sync to latest git commit: 1efc1ece0d1e282b1cf4f371d2f7c4098113c098

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
