# Volatility
# Copyright (C) 2007,2008 Volatile Systems
#
# Original Source:
# Volatools Basic
# Copyright (C) 2007 Komoku, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#

"""
@author:       AAron Walters
@license:      GNU General Public License 2.0 or later
@contact:      awalters@volatilesystems.com
@organization: Volatile Systems
"""

xpsp2types = { \
  '_LIST_ENTRY' : [ 0x8, { \
    'Flink' : [ 0x0, ['pointer', ['_LIST_ENTRY']]], \
    'Blink' : [ 0x4, ['pointer', ['_LIST_ENTRY']]], \
} ], \
  '_KUSER_SHARED_DATA' : [ 0x338, { \
    'SystemTime' : [ 0x14, ['_KSYSTEM_TIME']], \
    'TimeZoneBias' : [ 0x20, ['_KSYSTEM_TIME']], \
    'SuiteMask' : [ 0x2d0, ['unsigned long']], \
    'NumberOfPhysicalPages' : [ 0x2e8, ['unsigned long']], \
} ], \
  '_LARGE_INTEGER' : [ 0x8, { \
    'LowPart' : [ 0x0, ['unsigned long']], \
    'HighPart' : [ 0x4, ['long']], \
} ], \
  '_KSYSTEM_TIME' : [ 0xc, { \
    'LowPart' : [ 0x0, ['unsigned long']], \
    'High1Time' : [ 0x4, ['long']], \
} ], \
  '_EPROCESS' : [ 0x260, { \
    'Pcb' : [ 0x0, ['_KPROCESS']], \
    'CreateTime' : [ 0x70, ['_LARGE_INTEGER']], \
    'ExitTime' : [ 0x78, ['_LARGE_INTEGER']], \
    'UniqueProcessId' : [ 0x84, ['pointer', ['void']]], \
    'ActiveProcessLinks' : [ 0x88, ['_LIST_ENTRY']], \
    'VirtualSize' : [ 0xb0, ['unsigned long']], \
    'ObjectTable' : [ 0xc4, ['pointer', ['_HANDLE_TABLE']]], \
    'WorkingSetLock' : [ 0xcc, ['_FAST_MUTEX']], \
    'AddressCreationLock' : [ 0xf0, ['_FAST_MUTEX']], \
    'VadRoot' : [ 0x11c, ['pointer', ['void']]], \
    'InheritedFromUniqueProcessId' : [ 0x14c, ['pointer', ['void']]], \
    'ImageFileName' : [ 0x174, ['array', 16,['unsigned char']]], \
    'ThreadListHead' : [ 0x190, ['_LIST_ENTRY']], \
    'ActiveThreads' : [ 0x1a0, ['unsigned long']], \
    'Peb' : [ 0x1b0, ['pointer', ['_PEB']]], \
    'ExitStatus' : [ 0x24c, ['long']], \
} ], \
  '_KPROCESS' : [ 0x6c, { \
    'Header' : [ 0x0, ['_DISPATCHER_HEADER']], \
    'DirectoryTableBase' : [ 0x18, ['array', 2,['unsigned long']]], \
} ], \
  '_PEB' : [ 0x210, { \
    'ImageBaseAddress' : [ 0x8, ['pointer', ['void']]], \
    'Ldr' : [ 0xc, ['pointer', ['_PEB_LDR_DATA']]], \
    'ProcessParameters' : [ 0x10, ['pointer', ['_RTL_USER_PROCESS_PARAMETERS']]], \
    'NumberOfProcessors' : [ 0x64, ['unsigned long']], \
    'OSMajorVersion' : [ 0xa4, ['unsigned long']], \
    'OSMinorVersion' : [ 0xa8, ['unsigned long']], \
    'OSBuildNumber' : [ 0xac, ['unsigned short']], \
    'CSDVersion' : [ 0x1f0, ['_UNICODE_STRING']], \
} ], \
  '_RTL_USER_PROCESS_PARAMETERS' : [ 0x290, { \
    'CommandLine' : [ 0x40, ['_UNICODE_STRING']], \
} ], \
  '_UNICODE_STRING' : [ 0x8, { \
    'Length' : [ 0x0, ['unsigned short']], \
    'Buffer' : [ 0x4, ['pointer', ['unsigned short']]], \
} ], \
  '_PEB_LDR_DATA' : [ 0x28, { \
    'InLoadOrderModuleList' : [ 0xc, ['_LIST_ENTRY']], \
} ], \
  '_LDR_MODULE' : [ 0x48, { \
    'InLoadOrderModuleList' : [ 0x0, ['_LIST_ENTRY']], \
    'BaseAddress' : [ 0x18, ['pointer', ['void']]], \
    'SizeOfImage' : [ 0x20, ['unsigned long']], \
    'FullDllName' : [ 0x24, ['_UNICODE_STRING']], \
    'ModuleName'  : [ 0x2c, ['_UNICODE_STRING']], \
} ], \
  '_ADDRESS_OBJECT' : [ 0x68, { \
    'Next' : [ 0x0, ['pointer', ['_ADDRESS_OBJECT']]], \
    'LocalIpAddress' : [ 0x0c, ['unsigned long']], \
    'LocalPort' : [ 0x30, ['unsigned short']], \
    'Protocol'  : [ 0x32, ['unsigned short']], \
    'Pid' : [ 0x148, ['unsigned long']], \
    'CreateTime' : [ 0x158, ['_LARGE_INTEGER']], \
} ], \
  '_TCPT_OBJECT' : [ 0x20, { \
  'Next' : [ 0x0, ['pointer', ['_TCPT_OBJECT']]], \
  'RemoteIpAddress' : [ 0xc, ['unsigned long']], \
  'LocalIpAddress' : [ 0x10, ['unsigned long']], \
  'RemotePort' : [ 0x14, ['unsigned short']], \
  'LocalPort' : [ 0x16, ['unsigned short']], \
  'Pid' : [ 0x18, ['unsigned long']], \
} ], \
  '_HANDLE_TABLE' : [ 0x44, { \
    'TableCode' : [ 0x0, ['unsigned long']], \
    'UniqueProcessId' : [ 0x8, ['pointer', ['void']]], \
    'HandleTableList' : [ 0x1c, ['_LIST_ENTRY']], \
    'HandleCount' : [ 0x3c, ['long']], \
} ], \
  '_HANDLE_TABLE_ENTRY' : [ 0x8, { \
    'Object' : [ 0x0, ['pointer', ['void']]], \
} ], \
  '_OBJECT_HEADER' : [ 0x20, { \
    'Type' : [ 0x8, ['pointer', ['_OBJECT_TYPE']]], \
    'Body' : [ 0x18, ['_QUAD']], \
} ], \
  '_OBJECT_TYPE' : [ 0x190, { \
    'Name' : [ 0x40, ['_UNICODE_STRING']], \
} ], \
  '_FILE_OBJECT' : [ 0x70, { \
    'Type' : [ 0x0, ['short']], \
    'FileName' : [ 0x30, ['_UNICODE_STRING']], \
} ], \
'_KPCR' : [  0xd70, { \
  'KdVersionBlock' : [ 0x34, ['pointer', ['void']]], \
} ], \
  '_KDDEBUGGER_DATA32' : [ 0x44, { \
  'PsLoadedModuleList' : [ 0x70, ['unsigned long']], \
  'PsActiveProcessHead' : [ 0x78, ['unsigned long']], \
} ], \
  '_KDDEBUGGER_DATA64' : [ 0x44, { \
  'PsLoadedModuleList' : [ 0x48, ['unsigned long']], \
  'PsActiveProcessHead' : [ 0x50, ['unsigned long']], \
  'MmPfnDatabase' : [ 0xC0, ['unsigned long']], \
} ], \
'_DBGKD_GET_VERSION64' : [  0x2a, { \
  'DebuggerDataList' : [ 0x20, ['unsigned long']], \
} ], \
'_MMVAD_LONG' : [  0x34, { \
  'StartingVpn' : [ 0x0, ['unsigned long']], \
  'EndingVpn' : [ 0x4, ['unsigned long']], \
  'Parent' : [ 0x8, ['pointer', ['_MMVAD']]], \
  'LeftChild' : [ 0xc, ['pointer', ['_MMVAD']]], \
  'RightChild' : [ 0x10, ['pointer', ['_MMVAD']]], \
  'u' : [ 0x14, ['__unnamed']], \
  'ControlArea' : [ 0x18, ['pointer', ['_CONTROL_AREA']]], \
  'FirstPrototypePte' : [ 0x1c, ['pointer', ['_MMPTE']]], \
  'LastContiguousPte' : [ 0x20, ['pointer', ['_MMPTE']]], \
  'u2' : [ 0x24, ['__unnamed']], \
  'u3' : [ 0x28, ['__unnamed']], \
  'u4' : [ 0x30, ['__unnamed']], \
} ], \
'_MMVAD' : [  0x28, { \
  'StartingVpn' : [ 0x0, ['unsigned long']], \
  'EndingVpn' : [ 0x4, ['unsigned long']], \
  'Parent' : [ 0x8, ['pointer', ['_MMVAD']]], \
  'LeftChild' : [ 0xc, ['pointer', ['_MMVAD']]], \
  'RightChild' : [ 0x10, ['pointer', ['_MMVAD']]], \
  'u' : [ 0x14, ['__unnamed']], \
  'ControlArea' : [ 0x18, ['pointer', ['_CONTROL_AREA']]], \
  'FirstPrototypePte' : [ 0x1c, ['pointer', ['_MMPTE']]], \
  'LastContiguousPte' : [ 0x20, ['pointer', ['_MMPTE']]], \
  'u2' : [ 0x24, ['__unnamed']], \
} ], \
'_MMVAD_SHORT' : [  0x18, { \
  'StartingVpn' : [ 0x0, ['unsigned long']], \
  'EndingVpn' : [ 0x4, ['unsigned long']], \
  'Parent' : [ 0x8, ['pointer', ['_MMVAD']]], \
  'LeftChild' : [ 0xc, ['pointer', ['_MMVAD']]], \
  'RightChild' : [ 0x10, ['pointer', ['_MMVAD']]], \
  'u' : [ 0x14, ['__unnamed']], \
} ], \
'_CONTROL_AREA' : [  0x30, { \
  'Segment' : [ 0x0, ['pointer', ['_SEGMENT']]], \
  'DereferenceList' : [ 0x4, ['_LIST_ENTRY']], \
  'NumberOfSectionReferences' : [ 0xc, ['unsigned long']], \
  'NumberOfPfnReferences' : [ 0x10, ['unsigned long']], \
  'NumberOfMappedViews' : [ 0x14, ['unsigned long']], \
  'NumberOfSubsections' : [ 0x18, ['unsigned short']], \
  'FlushInProgressCount' : [ 0x1a, ['unsigned short']], \
  'NumberOfUserReferences' : [ 0x1c, ['unsigned long']], \
  'u' : [ 0x20, ['__unnamed']], \
  'FilePointer' : [ 0x24, ['pointer', ['_FILE_OBJECT']]], \
  'WaitingForDeletion' : [ 0x28, ['pointer', ['_EVENT_COUNTER']]], \
  'ModifiedWriteCount' : [ 0x2c, ['unsigned short']], \
  'NumberOfSystemCacheViews' : [ 0x2e, ['unsigned short']], \
} ], \
'_POOL_HEADER' : [  0x8, { \
  'Ulong1' : [ 0x0, ['unsigned long']], \
  'BlockSize': [ 0x2, ['unsigned short']], \
  'PoolType': [ 0x2, ['unsigned short']], \
  'ProcessBilled' : [ 0x4, ['pointer', ['_EPROCESS']]], \
  'PoolTag' : [ 0x4, ['unsigned long']], \
  'AllocatorBackTraceIndex' : [ 0x4, ['unsigned short']], \
  'PoolTagHash' : [ 0x6, ['unsigned short']], \
} ], \
'_FAST_MUTEX' : [  0x20, { \
  'Event' : [ 0xc, ['_KEVENT']], \
} ], \
'_KEVENT' : [  0x10, { \
  'Header' : [ 0x0, ['_DISPATCHER_HEADER']], \
} ], \
'_DISPATCHER_HEADER' : [  0x10, { \
  'Type' : [ 0x0, ['unsigned char']], \
  'Size' : [ 0x2, ['unsigned char']], \
} ], \
'_ETHREAD' : [  0x258, { \
  'Tcb' : [ 0x0, ['_KTHREAD']], \
  'Cid' : [ 0x1ec, ['_CLIENT_ID']], \
  'LpcReplySemaphore' : [ 0x1f4, ['_KSEMAPHORE']], \
  'ThreadsProcess' : [ 0x220, ['pointer', ['_EPROCESS']]], \
  'StartAddress' : [ 0x224, ['pointer', ['void']]], \
} ], \
'_CLIENT_ID' : [  0x8, { \
  'UniqueProcess' : [ 0x0, ['pointer', ['void']]], \
  'UniqueThread' : [ 0x4, ['pointer', ['void']]], \
} ], \
'_KTHREAD' : [  0x1c0, { \
  'Header' : [ 0x0, ['_DISPATCHER_HEADER']], \
  'Timer' : [ 0xf0, ['_KTIMER']], \
  'SuspendSemaphore' : [ 0x19c, ['_KSEMAPHORE']], \
} ], \
'_KTIMER' : [  0x28, { \
  'Header' : [ 0x0, ['_DISPATCHER_HEADER']], \
} ], \
'_KSEMAPHORE' : [  0x14, { \
  'Header' : [ 0x0, ['_DISPATCHER_HEADER']], \
} ], \
'_PHYSICAL_MEMORY_RUN' : [ 0x8, { \
  'BasePage' : [ 0x0, ['unsigned long']], \
  'PageCount' : [ 0x4, ['unsigned long']], \
} ], \
'_PHYSICAL_MEMORY_DESCRIPTOR' : [ 0x10, { \
  'NumberOfRuns' : [ 0x0, ['unsigned long']], \
  'NumberOfPages' : [ 0x4, ['unsigned long']], \
  'Run' : [ 0x8, ['array', 1,['_PHYSICAL_MEMORY_RUN']]], \
} ], \
'_DMP_HEADER' : [ 0x1000, { \
  'Signature' : [ 0x0, ['array', 4,['unsigned char']]], \
  'ValidDump' : [ 0x4, ['array', 4,['unsigned char']]], \
  'MajorVersion' : [ 0x8, ['unsigned long']], \
  'MinorVersion' : [ 0xc, ['unsigned long']], \
  'DirectoryTableBase' : [ 0x10, ['unsigned long']], \
  'PfnDataBase' : [ 0x14, ['unsigned long']], \
  'PsLoadedModuleList' : [ 0x18, ['unsigned long']], \
  'PsActiveProcessHead' : [ 0x1c, ['unsigned long']], \
  'MachineImageType' : [ 0x20, ['unsigned long']], \
  'NumberProcessors' : [ 0x24, ['unsigned long']], \
  'BugCheckCode' : [ 0x28, ['unsigned long']], \
  'BugCheckCodeParameter' : [ 0x2c, ['array', 4,['unsigned long']]], \
  'VersionUser' : [ 0x3c, ['array', 32,['unsigned char']]], \
  'PaeEnabled' : [ 0x5c, ['unsigned char']], \
  'KdSecondaryVersion' : [ 0x5d, ['unsigned char']], \
  'VersionUser' : [ 0x5e, ['array', 2,['unsigned char']]], \
  'KdDebuggerDataBlock' : [ 0x60, ['unsigned long']], \
  'PhysicalMemoryBlockBuffer' : [ 0x64, ['_PHYSICAL_MEMORY_DESCRIPTOR']], \
  'ContextRecord' : [ 0x320, ['array', 1200,['unsigned char']]], \
  'Exception' : [ 0x7d0, ['_EXCEPTION_RECORD32']], \
  'Comment' : [ 0x820, ['array', 128,['unsigned char']]], \
  'DumpType' : [ 0xf88, ['unsigned long']], \
  'MiniDumpFields' : [ 0xf8c, ['unsigned long']], \
  'SecondaryDataState' : [ 0xf90, ['unsigned long']], \
  'ProductType' : [ 0xf94, ['unsigned long']], \
  'SuiteMask' : [ 0xf98, ['unsigned long']], \
  'WriterStatus' : [ 0xf9c, ['unsigned long']], \
  'RequiredDumpSpace' : [ 0xfa0, ['unsigned __int64']], \
  'SystemUpTime' : [ 0xfb8, ['unsigned __int64']], \
  'SystemTime' : [ 0xfc0, ['unsigned __int64']], \
  'reserved3' : [ 0xfc8, ['array', 56,['unsigned char']]], \
} ], \
  '_TEB' : [ 0xfb8, { \
    'ProcessEnvironmentBlock' : [ 0x30, ['pointer', ['_PEB']]], \
} ], \
  '_KPROCESSOR_STATE' : [ 0x320, { \
    'SpecialRegisters' : [ 0x2cc, ['_KSPECIAL_REGISTERS']], \
} ], \
  '_KSPECIAL_REGISTERS' : [ 0x54, { \
    'Cr0' : [ 0x0, ['unsigned long']], \
    'Cr3' : [ 0x8, ['unsigned long']], \
    'Cr4' : [ 0xc, ['unsigned long']], \
    'Gdtr' : [ 0x28, ['_DESCRIPTOR']], \
} ], \
    '_DESCRIPTOR' : [ 0x8, { \
    'Pad' : [ 0x0, ['unsigned short']], \
    'Limit' : [ 0x2, ['unsigned short']], \
    'Base' : [ 0x4, ['unsigned long']], \
} ], \
'_CM_KEY_BODY' : [  0x44, { \
  'Type' : [ 0x0, ['unsigned long']], \
  'KeyControlBlock' : [ 0x4, ['pointer', ['_CM_KEY_CONTROL_BLOCK']]], \
} ], \
'_CM_KEY_CONTROL_BLOCK' : [  0x48, { \
  'ParentKcb' : [ 0x18, ['pointer', ['_CM_KEY_CONTROL_BLOCK']]], \
  'NameBlock' : [ 0x1c, ['pointer', ['_CM_NAME_CONTROL_BLOCK']]], \
  'KcbLastWriteTime' : [ 0x38, ['_LARGE_INTEGER']], \
} ], \
'_CM_NAME_CONTROL_BLOCK' : [  0x10, { \
  'NameLength' : [ 0xc, ['unsigned short']], \
  'Name' : [ 0xe, ['array', 1,['unsigned short']]], \
} ], \
'_IMAGE_DOS_HEADER' : [  0x40, { \
  'e_lfanew' : [ 0x3c, ['long']], \
} ], \
'_IMAGE_NT_HEADERS' : [  0xf8, { \
  'FileHeader' : [ 0x4, ['_IMAGE_FILE_HEADER']], \
  'OptionalHeader' : [ 0x18, ['_IMAGE_OPTIONAL_HEADER']], \
} ], \
'_IMAGE_OPTIONAL_HEADER' : [  0xe0, { \
  'SectionAlignment' : [ 0x20, ['unsigned long']], \
  'FileAlignment' : [ 0x24, ['unsigned long']], \
  'SizeOfImage' : [ 0x38, ['unsigned long']], \
  'SizeOfHeaders' : [ 0x3c, ['unsigned long']], \
} ], \
'_IMAGE_FILE_HEADER' : [  0x14, { \
  'NumberOfSections' : [ 0x2, ['unsigned short']], \
  'SizeOfOptionalHeader' : [ 0x10, ['unsigned short']], \
} ], \
  '__misc' : [ 0x4, {
    'PhysicalAddress' : [ 0x0, ['unsigned long']],
    'VirtualSize' : [ 0x0, ['unsigned long']],
} ],
'_IMAGE_SECTION_HEADER' : [  0x28, { \
  'Name' : [ 0x0, ['array', 8,['unsigned char']]], \
  'Misc' : [ 0x8, ['__misc']],
  'VirtualAddress' : [ 0xc, ['unsigned long']], \
  'SizeOfRawData' : [ 0x10, ['unsigned long']], \
  'PointerToRawData' : [ 0x14, ['unsigned long']], \
} ], \
'_LDR_DATA_TABLE_ENTRY' : [ 0x50, { \
    'InLoadOrderLinks' : [ 0x0, ['_LIST_ENTRY']], \
    'InMemoryOrderLinks' : [ 0x8, ['_LIST_ENTRY']], \
    'InInitializationOrderLinks' : [ 0x10, ['_LIST_ENTRY']], \
    'DllBase' : [ 0x18, ['pointer', ['void']]], \
    'EntryPoint' : [ 0x1c, ['pointer', ['void']]], \
    'SizeOfImage' : [ 0x20, ['unsigned long']], \
    'FullDllName' : [ 0x24, ['_UNICODE_STRING']], \
    'BaseDllName' : [ 0x2c, ['_UNICODE_STRING']], \
} ], \

## These are registry related types
  '_CM_KEY_NODE' : [ 0x50, {
    'Signature' : [ 0x0, ['String', dict(length=2)]],
    'Flags' : [ 0x2, ['unsigned short']],
    'LastWriteTime' : [ 0x4, ['WinTimeStamp', {}]],
    'Spare' : [ 0xc, ['unsigned long']],
    'Parent' : [ 0x10, ['unsigned long']],
    'SubKeyCounts' : [ 0x14, ['array', 2, ['unsigned long']]],
    'SubKeyLists' : [ 0x1c, ['array', 2, ['unsigned long']]],
    'ValueList' : [ 0x24, ['_CHILD_LIST']],
    'ChildHiveReference' : [ 0x1c, ['_CM_KEY_REFERENCE']],
    'Security' : [ 0x2c, ['unsigned long']],
    'Class' : [ 0x30, ['unsigned long']],
    'MaxNameLen' : [ 0x34, ['unsigned long']],
    'MaxClassLen' : [ 0x38, ['unsigned long']],
    'MaxValueNameLen' : [ 0x3c, ['unsigned long']],
    'MaxValueDataLen' : [ 0x40, ['unsigned long']],
    'WorkVar' : [ 0x44, ['unsigned long']],
    'NameLength' : [ 0x48, ['unsigned short']],
    'ClassLength' : [ 0x4a, ['unsigned short']],
    'Name' : [ 0x4c, ['String', dict(length=lambda x: x.NameLength)]],
} ],
  '_CM_KEY_REFERENCE' : [ 0x8, {
    'KeyCell' : [ 0x0, ['unsigned long']],
    'KeyHive' : [ 0x4, ['pointer', ['_HHIVE']]],
} ],
  '_CHILD_LIST' : [ 0x8, {
    'Count' : [ 0x0, ['unsigned long']],
    'List' : [ 0x4, ['pointer', ['array', lambda x: x.Count,
                                 ['pointer', ['_CM_KEY_VALUE']]]]],
} ],
  '_CM_KEY_SECURITY' : [ 0x28, {
    'Signature' : [ 0x0, ['unsigned short']],
    'Reserved' : [ 0x2, ['unsigned short']],
    'Flink' : [ 0x4, ['unsigned long']],
    'Blink' : [ 0x8, ['unsigned long']],
    'ReferenceCount' : [ 0xc, ['unsigned long']],
    'DescriptorLength' : [ 0x10, ['unsigned long']],
    'Descriptor' : [ 0x14, ['_SECURITY_DESCRIPTOR_RELATIVE']],
} ],
  '_SECURITY_DESCRIPTOR_RELATIVE' : [ 0x14, {
    'Revision' : [ 0x0, ['unsigned char']],
    'Sbz1' : [ 0x1, ['unsigned char']],
    'Control' : [ 0x2, ['unsigned short']],
    'Owner' : [ 0x4, ['unsigned long']],
    'Group' : [ 0x8, ['unsigned long']],
    'Sacl' : [ 0xc, ['unsigned long']],
    'Dacl' : [ 0x10, ['unsigned long']],
} ],
  '_CM_KEY_VALUE' : [ 0x18, {
    'Signature' : [ 0x0, ['String', dict(length=2)]],
    'NameLength' : [ 0x2, ['unsigned short']],
    'DataLength' : [ 0x4, ['unsigned long']],
    'Data' : [ 0x8, ['unsigned long']],
    'Type' : [ 0xc, ['unsigned long']],
    'Flags' : [ 0x10, ['unsigned short']],
    'Spare' : [ 0x12, ['unsigned short']],
    'Name' : [ 0x14, ['String', dict(length=lambda x: x.NameLength)]],
} ],
  '_CM_KEY_INDEX' : [ 0x8, {
    'Signature' : [ 0x0, ['String', dict(length=2)]],
    'Count' : [ 0x2, ['unsigned short']],
    'List' : [ 0x4, ['array', lambda x: 2*x.Count.v(), ['pointer', ['_CM_KEY_NODE']]]],
} ],
  '_CMHIVE' : [ 0x49c, {
    'Hive' : [ 0x0, ['_HHIVE']],
    'FileHandles' : [ 0x210, ['array', 3, ['pointer', ['void']]]],
    'NotifyList' : [ 0x21c, ['_LIST_ENTRY']],
    'HiveList' : [ 0x224, ['_LIST_ENTRY']],
    'HiveLock' : [ 0x22c, ['pointer', ['_FAST_MUTEX']]],
    'ViewLock' : [ 0x230, ['pointer', ['_FAST_MUTEX']]],
    'LRUViewListHead' : [ 0x234, ['_LIST_ENTRY']],
    'PinViewListHead' : [ 0x23c, ['_LIST_ENTRY']],
    'FileObject' : [ 0x244, ['pointer', ['_FILE_OBJECT']]],
    'FileFullPath' : [ 0x248, ['_UNICODE_STRING']],
    'FileUserName' : [ 0x250, ['_UNICODE_STRING']],
    'MappedViews' : [ 0x258, ['unsigned short']],
    'PinnedViews' : [ 0x25a, ['unsigned short']],
    'UseCount' : [ 0x25c, ['unsigned long']],
    'SecurityCount' : [ 0x260, ['unsigned long']],
    'SecurityCacheSize' : [ 0x264, ['unsigned long']],
    'SecurityHitHint' : [ 0x268, ['long']],
    'SecurityCache' : [ 0x26c, ['pointer', ['_CM_KEY_SECURITY_CACHE_ENTRY']]],
    'SecurityHash' : [ 0x270, ['array', 64, ['_LIST_ENTRY']]],
    'UnloadEvent' : [ 0x470, ['pointer', ['_KEVENT']]],
    'RootKcb' : [ 0x474, ['pointer', ['_CM_KEY_CONTROL_BLOCK']]],
    'Frozen' : [ 0x478, ['unsigned char']],
    'UnloadWorkItem' : [ 0x47c, ['pointer', ['_WORK_QUEUE_ITEM']]],
    'GrowOnlyMode' : [ 0x480, ['unsigned char']],
    'GrowOffset' : [ 0x484, ['unsigned long']],
    'KcbConvertListHead' : [ 0x488, ['_LIST_ENTRY']],
    'KnodeConvertListHead' : [ 0x490, ['_LIST_ENTRY']],
    'CellRemapArray' : [ 0x498, ['pointer', ['_CM_CELL_REMAP_BLOCK']]],
} ],
  '_HHIVE' : [ 0x210, {
    'Signature' : [ 0x0, ['unsigned long']],
     'GetCellRoutine' : [ 0x4, ['pointer', ['void']]],
     'ReleaseCellRoutine' : [ 0x8, ['pointer', ['void']]],
     'Allocate' : [ 0xc, ['pointer', ['void']]],
     'Free' : [ 0x10, ['pointer', ['void']]],
     'FileSetSize' : [ 0x14, ['pointer', ['void']]],
     'FileWrite' : [ 0x18, ['pointer', ['void']]],
     'FileRead' : [ 0x1c, ['pointer', ['void']]],
     'FileFlush' : [ 0x20, ['pointer', ['void']]],
    'BaseBlock' : [ 0x24, ['pointer', ['_HBASE_BLOCK']]],
    'DirtyVector' : [ 0x28, ['_RTL_BITMAP']],
    'DirtyCount' : [ 0x30, ['unsigned long']],
    'DirtyAlloc' : [ 0x34, ['unsigned long']],
    'RealWrites' : [ 0x38, ['unsigned char']],
    'Cluster' : [ 0x3c, ['unsigned long']],
    'Flat' : [ 0x40, ['unsigned char']],
    'ReadOnly' : [ 0x41, ['unsigned char']],
    'Log' : [ 0x42, ['unsigned char']],
    'HiveFlags' : [ 0x44, ['unsigned long']],
    'LogSize' : [ 0x48, ['unsigned long']],
    'RefreshCount' : [ 0x4c, ['unsigned long']],
    'StorageTypeCount' : [ 0x50, ['unsigned long']],
    'Version' : [ 0x54, ['unsigned long']],
    'Storage' : [ 0x58, ['array', 2, ['_DUAL']]],
} ],
  '_HBASE_BLOCK' : [ 0x1000, {
    'Signature' : [ 0x0, ['unsigned long']],
    'Sequence1' : [ 0x4, ['unsigned long']],
    'Sequence2' : [ 0x8, ['unsigned long']],
    'TimeStamp' : [ 0xc, ['_LARGE_INTEGER']],
    'Major' : [ 0x14, ['unsigned long']],
    'Minor' : [ 0x18, ['unsigned long']],
    'Type' : [ 0x1c, ['unsigned long']],
    'Format' : [ 0x20, ['unsigned long']],
    'RootCell' : [ 0x24, ['unsigned long']],
    'Length' : [ 0x28, ['unsigned long']],
    'Cluster' : [ 0x2c, ['unsigned long']],
    'FileName' : [ 0x30, ['array', 64, ['unsigned char']]],
    'Reserved1' : [ 0x70, ['array', 99, ['unsigned long']]],
    'CheckSum' : [ 0x1fc, ['unsigned long']],
    'Reserved2' : [ 0x200, ['array', 894, ['unsigned long']]],
    'BootType' : [ 0xff8, ['unsigned long']],
    'BootRecover' : [ 0xffc, ['unsigned long']],
} ],
  '_DUAL' : [ 0xdc, {
    'Length' : [ 0x0, ['unsigned long']],
    'Map' : [ 0x4, ['pointer', ['_HMAP_DIRECTORY']]],
    'SmallDir' : [ 0x8, ['pointer', ['_HMAP_TABLE']]],
    'Guard' : [ 0xc, ['unsigned long']],
    'FreeDisplay' : [ 0x10, ['array', 24, ['_RTL_BITMAP']]],
    'FreeSummary' : [ 0xd0, ['unsigned long']],
    'FreeBins' : [ 0xd4, ['_LIST_ENTRY']],
} ],
  '_HMAP_DIRECTORY' : [ 0x1000, {
    'Directory' : [ 0x0, ['array', 1024, ['pointer', ['_HMAP_TABLE']]]],
} ],
  '_HMAP_TABLE' : [ 0x2000, {
    'Table' : [ 0x0, ['array', 512, ['_HMAP_ENTRY']]],
} ],
  '_HMAP_ENTRY' : [ 0x10, {
    'BlockAddress' : [ 0x0, ['unsigned long']],
    'BinAddress' : [ 0x4, ['unsigned long']],
    'CmView' : [ 0x8, ['pointer', ['_CM_VIEW_OF_FILE']]],
    'MemAlloc' : [ 0xc, ['unsigned long']],
} ],
  '_CM_KEY_SECURITY_CACHE_ENTRY' : [ 0x8, {
    'Cell' : [ 0x0, ['unsigned long']],
    'CachedSecurity' : [ 0x4, ['pointer', ['_CM_KEY_SECURITY_CACHE']]],
} ],
  '_CM_KEY_SECURITY_CACHE' : [ 0x28, {
    'Cell' : [ 0x0, ['unsigned long']],
    'ConvKey' : [ 0x4, ['unsigned long']],
    'List' : [ 0x8, ['_LIST_ENTRY']],
    'DescriptorLength' : [ 0x10, ['unsigned long']],
    'Descriptor' : [ 0x14, ['_SECURITY_DESCRIPTOR_RELATIVE']],
} ],
  '_CM_CELL_REMAP_BLOCK' : [ 0x8, {
    'OldCell' : [ 0x0, ['unsigned long']],
    'NewCell' : [ 0x4, ['unsigned long']],
} ],
  '_LARGE_INTEGER' : [ 0x8, {
    'LowPart' : [ 0x0, ['unsigned long']],
    'HighPart' : [ 0x4, ['long']],
    'QuadPart' : [ 0x0, ['long long']],
} ],
    '_IMAGE_HIBER_HEADER' : [ 0xbc, { \
    'Signature' : [ 0x0, ['array', 4,['unsigned char']]], \
    'SystemTime' : [ 0x20, ['_LARGE_INTEGER']], \
    'FirstTablePage' : [ 0x58, ['unsigned long']], \
} ], \
    'MEMORY_RANGE_ARRAY_LINK' : [ 0x10, { \
    'NextTable' : [ 0x4, ['unsigned long']], \
    'EntryCount' : [ 0xc, ['unsigned long']], \
} ], \
    'MEMORY_RANGE_ARRAY_RANGE' : [ 0x10, { \
    'StartPage' : [ 0x4, ['unsigned long']], \
    'EndPage' : [ 0x8, ['unsigned long']], \
} ], \
    '_MEMORY_RANGE_ARRAY' : [ 0x20, { \
    'MemArrayLink' : [ 0x0, ['MEMORY_RANGE_ARRAY_LINK']], \
    'RangeTable': [ 0x10, ['array', lambda x: x.MemArrayLink.EntryCount,
                           ['MEMORY_RANGE_ARRAY_RANGE']]],
} ], \
  '_KGDTENTRY' : [  0x8 , { \
  'BaseLow' : [ 0x2 , ['unsigned short']], \
  'BaseMid' : [ 0x4, ['unsigned char']], \
  'BaseHigh' : [ 0x7, ['unsigned char']], \
} ], \
'_IMAGE_XPRESS_HEADER' : [  0x20 , { \
  'u09' : [ 0x9, ['unsigned char']], \
  'u0A' : [ 0xA, ['unsigned char']], \
  'u0B' : [ 0xB, ['unsigned char']], \
} ], \

## These types are for crash dumps
    '_PHYSICAL_MEMORY_RUN' : [ 0x8, { \
    'BasePage' : [ 0x0, ['unsigned long']], \
    'PageCount' : [ 0x4, ['unsigned long']], \
} ], \
    '_PHYSICAL_MEMORY_DESCRIPTOR' : [ 0x10, { \
    'NumberOfRuns' : [ 0x0, ['unsigned long']], \
    'NumberOfPages' : [ 0x4, ['unsigned long']], \
    'Run' : [ 0x8, ['array', 1,['_PHYSICAL_MEMORY_RUN']]], \
} ], \
  '_DMP_HEADER' : [ 0x1000, { \
    'Signature' : [ 0x0, ['array', 4,['unsigned char']]], \
    'ValidDump' : [ 0x4, ['array', 4,['unsigned char']]], \
    'MajorVersion' : [ 0x8, ['unsigned long']], \
    'MinorVersion' : [ 0xc, ['unsigned long']], \
    'DirectoryTableBase' : [ 0x10, ['unsigned long']], \
    'PfnDataBase' : [ 0x14, ['unsigned long']], \
    'PsLoadedModuleList' : [ 0x18, ['unsigned long']], \
    'PsActiveProcessHead' : [ 0x1c, ['unsigned long']], \
    'MachineImageType' : [ 0x20, ['unsigned long']], \
    'NumberProcessors' : [ 0x24, ['unsigned long']], \
    'BugCheckCode' : [ 0x28, ['unsigned long']], \
    'BugCheckCodeParameter' : [ 0x2c, ['array', 4,['unsigned long']]], \
    'VersionUser' : [ 0x3c, ['array', 32,['unsigned char']]], \
    'PaeEnabled' : [ 0x5c, ['unsigned char']], \
    'KdSecondaryVersion' : [ 0x5d, ['unsigned char']], \
    'VersionUser' : [ 0x5e, ['array', 2,['unsigned char']]], \
    'KdDebuggerDataBlock' : [ 0x60, ['unsigned long']], \
    'PhysicalMemoryBlockBuffer' : [ 0x64, ['_PHYSICAL_MEMORY_DESCRIPTOR']], \
    'ContextRecord' : [ 0x320, ['array', 1200,['unsigned char']]], \
    'Exception' : [ 0x7d0, ['_EXCEPTION_RECORD32']], \
    'Comment' : [ 0x820, ['array', 128,['unsigned char']]], \
    'DumpType' : [ 0xf88, ['unsigned long']], \
    'MiniDumpFields' : [ 0xf8c, ['unsigned long']], \
    'SecondaryDataState' : [ 0xf90, ['unsigned long']], \
    'ProductType' : [ 0xf94, ['unsigned long']], \
    'SuiteMask' : [ 0xf98, ['unsigned long']], \
    'WriterStatus' : [ 0xf9c, ['unsigned long']], \
    'RequiredDumpSpace' : [ 0xfa0, ['unsigned __int64']], \
    'SystemUpTime' : [ 0xfb8, ['unsigned __int64']], \
    'SystemTime' : [ 0xfc0, ['unsigned __int64']], \
    'reserved3' : [ 0xfc8, ['array', 56,['unsigned char']]], \
} ], \

}

