#!/usr/bin/env python3.4
#Copyright (c) 2018, The Linux Foundation. All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are
#met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
#    * Neither the name of The Linux Foundation nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT
#ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
#BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
#BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
#OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
#IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from acts.test_utils.tel.tel_voice_utils import two_phone_call_msim_short_seq,\
    phone_setup_voice_general_for_slot
from acts.test_decorators import test_tracker_info
from acts.test_utils.tel.TelephonyBaseTest import TelephonyBaseTest
from acts.test_utils.tel.tel_test_utils import multithread_func
from acts.test_utils.tel.tel_defines import MULTI_SIM_CONFIG
from google.tel.live.TelLiveVoiceTest import TelLiveVoiceTest



class TelLiveMSIMVoiceTest(TelLiveVoiceTest):
    
    def __init__(self, controllers):
        TelLiveVoiceTest.__init__(self, controllers)
        self.sim_config = {
                            "config":MULTI_SIM_CONFIG,
                            "number_of_sims":2
                        }
             
    
    @TelephonyBaseTest.tel_test_wrap
    #@test_tracker_info(uuid="fca3f9e1-447a-416f-9a9c-50b7161981bf")
    @test_tracker_info(uuid="Need more Information")
    def test_call_mo_voice_general(self):
        """ General voice to voice call.

        1. Make Sure PhoneA attached to voice network.
        2. Make Sure PhoneB attached to voice network.
        3. Call from PhoneA to PhoneB, accept on PhoneB, hang up on PhoneA.
        4. Call from PhoneA to PhoneB, accept on PhoneB, hang up on PhoneB.

        Returns:
            True if pass; False if fail.
        """
        ads = self.android_devices
        
        tasks = [(phone_setup_voice_general_for_slot, (self.log, ads[0],0)),
                 (phone_setup_voice_general_for_slot, (self.log, ads[1],0)),
                 (phone_setup_voice_general_for_slot, (self.log, ads[0],1)),
                 (phone_setup_voice_general_for_slot, (self.log, ads[1],1))
                 ]
        
        if not multithread_func(self.log, tasks):
            self.log.error("Phone Failed to Set Up Properly.")
            return False

        return two_phone_call_msim_short_seq(self.log, ads[0], None, None, ads[1],None, None,None)
