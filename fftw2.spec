#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fftw
Version  : 3.3.8
Release  : 32
URL      : http://www.fftw.org/fftw-3.3.8.tar.gz
Source0  : http://www.fftw.org/fftw-3.3.8.tar.gz
Summary  : fast Fourier transform library
Group    : Development/Tools
License  : GPL-2.0
Requires: fftw-bin = %{version}-%{release}
Requires: fftw-info = %{version}-%{release}
Requires: fftw-lib = %{version}-%{release}
Requires: fftw-license = %{version}-%{release}
Requires: fftw-man = %{version}-%{release}
BuildRequires : gfortran
BuildRequires : openmpi-dev
BuildRequires : openssh
BuildRequires : texinfo
Patch1: avx512-alignment.patch

%description
FFTW is a free collection of fast C routines for computing the
Discrete Fourier Transform in one or more dimensions.  It includes
complex, real, symmetric, and parallel transforms, and can handle
arbitrary array sizes efficiently.  FFTW is typically faster than
other publically-available FFT implementations, and is even
competitive with vendor-tuned libraries.  (See our web page
http://fftw.org/ for extensive benchmarks.)  To achieve this
performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

%package bin
Summary: bin components for the fftw package.
Group: Binaries
Requires: fftw-license = %{version}-%{release}

%description bin
bin components for the fftw package.


%package dev
Summary: dev components for the fftw package.
Group: Development
Requires: fftw-lib = %{version}-%{release}
Requires: fftw-bin = %{version}-%{release}
Provides: fftw-devel = %{version}-%{release}
Requires: fftw = %{version}-%{release}

%description dev
dev components for the fftw package.


%package info
Summary: info components for the fftw package.
Group: Default

%description info
info components for the fftw package.


%package lib
Summary: lib components for the fftw package.
Group: Libraries
Requires: fftw-license = %{version}-%{release}

%description lib
lib components for the fftw package.


%package license
Summary: license components for the fftw package.
Group: Default

%description license
license components for the fftw package.


%package man
Summary: man components for the fftw package.
Group: Default

%description man
man components for the fftw package.


%prep
%setup -q -n fftw-3.3.8
cd %{_builddir}/fftw-3.3.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586567660
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  -n ||:


%install
export SOURCE_DATE_EPOCH=1586567660
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fftw
cp %{_builddir}/fftw-3.3.8/COPYING %{buildroot}/usr/share/package-licenses/fftw/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/fftw-3.3.8/COPYRIGHT %{buildroot}/usr/share/package-licenses/fftw/1179609f742d35f1bcbf4ad694f371d64ee257ea
cp %{_builddir}/fftw-3.3.8/doc/html/License-and-Copyright.html %{buildroot}/usr/share/package-licenses/fftw/417539058454b49d5d54dce3c6f2ce2d766fa902
cp %{_builddir}/fftw-3.3.8/doc/license.texi %{buildroot}/usr/share/package-licenses/fftw/ee99393637fb0b0a5df385deac9040c5305f38b2
:
## install_append content
CFLAGS_IN="$CFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "
CXXFLAGS_IN="$CXXFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "

for build in \
# "single,--enable-float,--enable-sse2,--libdir=/usr/lib64" \
# "double,--enable-sse2,--libdir=/usr/lib64" \
"long-double,--enable-long-double,--libdir=/usr/lib64" \
"single-avx2,--enable-float,--enable-avx2,--enable-fma,--libdir=/usr/lib64/haswell" \
"double-avx2,--enable-avx2,--enable-fma,--libdir=/usr/lib64/haswell" \
# "single-avx512,--enable-float,--enable-avx2,--enable-avx512,--enable-fma,--libdir=/usr/lib64/haswell/avx512_1" \
# "double-avx512,--enable-avx2,--enable-avx512,--enable-fma,--libdir=/usr/lib64/haswell/avx512_1" \
# "single-mpi,--enable-mpi,--enable-float,--enable-sse2,--libdir=/usr/lib64"  \
# "double-mpi,--enable-mpi,--enable-sse2,--libdir=/usr/lib64" \
"long-double-mpi,--enable-mpi,--enable-long-double,--libdir=/usr/lib64" \
"single-avx2-mpi,--enable-mpi,--enable-float,--enable-avx2,--enable-fma,--libdir=/usr/lib64/haswell" \
"double-avx2-mpi,--enable-mpi,--enable-avx2,--enable-fma,--libdir=/usr/lib64/haswell" \
# "single-avx512-mpi,--enable-mpi,--enable-float,--enable-avx2,--enable-avx512,--enable-fma,--libdir=/usr/lib64/haswell/avx512_1" \
# "double-avx512-mpi,--enable-mpi,--enable-avx2,--enable-avx512,--enable-fma,--libdir=/usr/lib64/haswell/avx512_1" ; \
do
skip_test=0
dir=$(echo $build | cut -d, -f1)
flags=$(echo $build | cut -d, -f2- | sed 's/,/ /g')
lib_path=$(echo $build | cut -d= -f1 --complement)

if echo $flags | grep -q avx512; then
export CFLAGS="$CFLAGS_IN -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS_IN -march=skylake-avx512"
grep -q 'avx512[^ ]*' /proc/cpuinfo || skip_test=1
elif echo $flags | grep -q avx2; then
export CFLAGS="$CFLAGS_IN -march=haswell -mtune=haswell"
export CXXFLAGS="$CXXFLAGS_IN -march=haswell -mtune-haswell"
grep -q 'avx2[^ ]*' /proc/cpuinfo || skip_test=1
else
export CFLAGS="$CFLAGS_IN"
export CXXFLAGS="$CXXFLAGS_IN"
fi
--enable-long-double 
--enable-float 
mkdir build-$dir
pushd build-$dir
./configure --enable-static --enable-shared --enable-threads --enable-openmp --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-mpi --enable-long-double --enable-avx2 --enable-fma --libdir=/usr/lib64
./configure --enable-static --enable-shared --enable-threads --enable-openmp --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-mpi --enable-float --enable-avx2 --enable-fma --libdir=/usr/lib64
./configure --enable-static --enable-shared --enable-threads --enable-openmp --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-mpi --enable-avx2 --enable-fma --libdir=/usr/lib64
make V=1 %{?_smp_mflags}
%make_install
if [ $skip_test -eq 0 ]; then
echo "**** Testing $dir CFLAGS:$CFLAGS "
LD_LIBRARY_PATH="/insilications/apps/fftw-3.3.8/.libs:/insilications/apps/fftw-3.3.8:$LD_LIBRARY_PATH" make check
fi
popd
done

find %{buildroot}/usr/lib64 -name 'FFTW3*.cmake' -exec rm {} \;
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fftw-wisdom
/usr/bin/fftw-wisdom-to-conf
/usr/bin/fftwf-wisdom
/usr/bin/fftwl-wisdom

%files dev
%defattr(-,root,root,-)
/usr/include/fftw3-mpi.f03
/usr/include/fftw3-mpi.h
/usr/include/fftw3.f
/usr/include/fftw3.f03
/usr/include/fftw3.h
/usr/include/fftw3l-mpi.f03
/usr/include/fftw3l.f03
/usr/include/fftw3q.f03
/usr/lib64/haswell/avx512_1/libfftw3.so
/usr/lib64/haswell/avx512_1/libfftw3_mpi.so
/usr/lib64/haswell/avx512_1/libfftw3f.so
/usr/lib64/haswell/avx512_1/libfftw3f_mpi.so
/usr/lib64/haswell/libfftw3.so
/usr/lib64/haswell/libfftw3_mpi.so
/usr/lib64/haswell/libfftw3f.so
/usr/lib64/haswell/libfftw3f_mpi.so
/usr/lib64/libfftw3.so
/usr/lib64/libfftw3_mpi.so
/usr/lib64/libfftw3_omp.so
/usr/lib64/libfftw3_threads.so
/usr/lib64/libfftw3f.so
/usr/lib64/libfftw3f_mpi.so
/usr/lib64/libfftw3f_omp.so
/usr/lib64/libfftw3f_threads.so
/usr/lib64/libfftw3l.so
/usr/lib64/libfftw3l_mpi.so
/usr/lib64/libfftw3l_omp.so
/usr/lib64/libfftw3l_threads.so
/usr/lib64/pkgconfig/fftw3.pc
/usr/lib64/pkgconfig/fftw3f.pc
/usr/lib64/pkgconfig/fftw3l.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/fftw3.info
/usr/share/info/fftw3.info-1
/usr/share/info/fftw3.info-2

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libfftw3.so.3.5.8
/usr/lib64/haswell/libfftw3_mpi.so.3.5.8
/usr/lib64/haswell/libfftw3f.so.3.5.8
/usr/lib64/haswell/libfftw3f_mpi.so.3.5.8
/usr/lib64/libfftw3.so.3
/usr/lib64/libfftw3_mpi.so.3
/usr/lib64/libfftw3_mpi.so.3.5.8
/usr/lib64/libfftw3_omp.so.3
/usr/lib64/libfftw3_omp.so.3.5.8
/usr/lib64/libfftw3_threads.so.3
/usr/lib64/libfftw3_threads.so.3.5.8
/usr/lib64/libfftw3f.so.3
/usr/lib64/libfftw3f.so.3.5.8
/usr/lib64/libfftw3f_mpi.so.3
/usr/lib64/libfftw3f_mpi.so.3.5.8
/usr/lib64/libfftw3f_omp.so.3
/usr/lib64/libfftw3f_omp.so.3.5.8
/usr/lib64/libfftw3f_threads.so.3
/usr/lib64/libfftw3f_threads.so.3.5.8
/usr/lib64/libfftw3l.so.3
/usr/lib64/libfftw3l.so.3.5.8
/usr/lib64/libfftw3l_mpi.so.3
/usr/lib64/libfftw3l_mpi.so.3.5.8
/usr/lib64/libfftw3l_omp.so.3
/usr/lib64/libfftw3l_omp.so.3.5.8
/usr/lib64/libfftw3l_threads.so.3
/usr/lib64/libfftw3l_threads.so.3.5.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fftw/1179609f742d35f1bcbf4ad694f371d64ee257ea
/usr/share/package-licenses/fftw/417539058454b49d5d54dce3c6f2ce2d766fa902
/usr/share/package-licenses/fftw/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/fftw/ee99393637fb0b0a5df385deac9040c5305f38b2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fftw-wisdom-to-conf.1
/usr/share/man/man1/fftw-wisdom.1
/usr/share/man/man1/fftwf-wisdom.1
/usr/share/man/man1/fftwl-wisdom.1
