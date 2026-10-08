data = """
    if (zis(11))
    {
        enemy = ["oRustling,60,200,20,90", "oRustfish,18,300,75,150", "oMutateZ1C,14,400,150,250"];
    }
    else if (zis(12))
    {
        enemy = ["oRustling,55,200,20,100", "oRustfish,15,400,100,200", "oMutateZ1C,5,300,325,450", "oMutateZ1D,5,500,325,450", "oMutateZ1A,10,400,300,400"];
    }
    else if (zis(13))
    {
        enemy = ["oRustling,60,200,20,110", "oRustfish,18,400,100,200", "oMutateZ1C,7,300,300,400", "oMutateZ1D,7,500,300,400", "oMutateZ1A,10,500,300,400", "oMutateZ1B,12,500,400,600", "oCache,1,1000,200,900"];
    }
    else if (zis(14))
    {
        var rnd = RND_step();
        
        if ((SaveGet("GENERAL", "ACT3") == 1 && SaveGet("ENEMY", "EXOPOD") == -1) || oPlayer.upgrades[UnknownEnum.Value_21] == 1)
        {
            enemy = ["oBossExopod,1,270,0,0"];
        }
        else if (SaveGet("ENEMY", "EXOPOD") != -1)
        {
            if (rnd > (2/3))
                enemy = ["oBossExopod,1,270,0,0"];
            else if (rnd > (1/3))
                enemy = ["oBossCrusher,1,270,0,0"];
            else
                enemy = ["oBossNeedler,1,270,0,0"];
        }
        else if (rand > 0.5)
        {
            enemy = ["oBossCrusher,1,270,0,0"];
        }
        else
        {
            enemy = ["oBossNeedler,1,270,0,0"];
        }
    }
    
    if (zis(21))
    {
        if (global.zone2ALT)
            enemy = ["oCyclefish,15,200,200,400", "oSwaplet,50,100,100,200", "oSwapfish,25,400,100,300", "oBlobberlet,10,300,100,400"];
        else
            enemy = ["oFinlet,50,200,70,120", "oFinfish,40,400,130,200", "oAnemone,8,50,350,420", "oHusklet,12,300,250,300"];
    }
    else if (zis(22))
    {
        if (global.zone2ALT)
            enemy = ["oCyclefish,25,300,200,400", "oSwaplet,50,100,100,200", "oSwapfish,30,100,100,400", "oBlobberlet,12,200,300,500", "oMutateZ2B,5,400,470,650"];
        else
            enemy = ["oFinlet,45,200,60,150", "oFinfish,15,600,120,200", "oAnemone,6,100,370,650", "oMutateZ2,3,500,500,700", "oHusklet,10,300,250,355"];
    }
    else if (zis(23))
    {
        if (global.zone2ALT)
            enemy = ["oCyclefish,25,200,300,500", "oSwaplet,50,100,100,300", "oSwapfish,20,100,100,400", "oBlobberlet,10,0,400,600", "oBlobberfish,4,500,500,600", "oMutateZ2B,6,400,470,650", "oCache,1,1500,200,900"];
        else
            enemy = ["oFinlet,45,100,60,125", "oFinfish,15,600,120,250", "oAnemone,10,100,300,600", "oMutateZ2,8,500,400,600", "oHusklet,8,0,300,500", "oHuskeye,8,400,400,600", "oCache,1,1500,200,900"];
    }
    else if (zis(24))
    {
        if (global.zone2ALT)
        {
            if (RND_step() > 0.5 && SaveGet("ENEMY", "LIONEL") != -1)
                enemy = ["oBossCrab,1,190,0,0"];
            else
                enemy = ["oBossLionfish,1,270,0,0"];
        }
        else if (RND_step() > 0.5 && SaveGet("ENEMY", "POLYPA") != -1)
        {
            enemy = ["oBossSwordfish,1,270,0,0"];
        }
        else
        {
            enemy = ["oBossCoral,1,190,0,0"];
        }
    }
    
    if (zis(31))
    {
        enemy = ["oNode,150,150,20,150", "oSpotlet,16,100,150,250", "oMutateZ3B,20,500,200,300", "oMutateZ3A,15,600,150,300"];
    }
    else if (zis(32))
    {
        enemy = ["oNode,150,150,20,150", "oSpotlet,16,50,150,300", "oMutateZ3B,20,300,200,350", "oMutateZ3A,9,400,250,450", "oMutateZ3Eel,8,700,300,450"];
    }
    else if (zis(33))
    {
        enemy = ["oNode,150,150,20,150", "oSpotlet,15,50,300,400", "oMutateZ3B,15,300,250,350", "oMutateZ3A,6,400,350,450", "oMutateZ3Eel,3,700,300,400", "oMutateZ3Eel,3,2000,250,400", "oSpotfish,8,700,250,350", "oCache,1,1400,200,600"];
    }
    else if (zis(34))
    {
        if (exist(oPlayer) && oPlayer.upgrades[UnknownEnum.Value_21] == 1)
        {
            if (SaveGet("GENERAL", "ACT3") == 1)
            {
                enemy = ["oBossSpider,1,270,0,0"];
            }
            else if (SaveGet("QUEST", "EMITTER STREAK") >= 3)
            {
                enemy = ["oBossSpider,1,270,0,0"];
                SaveSet("AMPREY", "KEYWORDS", 1);
                SaveSet("DYNAMO", "KEYWORDS", 1);
            }
            else if (SaveGet("AMPREY", "KEYWORDS") > 0)
            {
                enemy = ["oBossGenerator,1,270,0,0"];
            }
            else
            {
                enemy = ["oBossEel,1,270,0,0"];
            }
        }
        else
        {
            var rnd = RND_step();
            
            if (SaveGet("GENERAL", "ACT3") == 1 && SaveGet("ENEMY", "ORBWEAVER") == -1)
                enemy = ["oBossSpider,1,270,0,0"];
            else if (rnd > (2/3) && SaveGet("GENERAL", "ACT3") == 1)
                enemy = ["oBossSpider,1,270,0,0"];
            else if (rnd > (1/3))
                enemy = ["oBossEel,1,270,0,0"];
            else
                enemy = ["oBossGenerator,1,270,0,0"];
        }
    }
    
    if (zisc(31, 33) && exist(oPlayer) && oPlayer.upgrades[UnknownEnum.Value_21] == 1)
    {
        if (SaveGet("GENERAL", "ACT3") == 1)
        {
            enemy = array_concat(enemy, ["oMentalNode,50,150,20,150"]);
        }
        else
        {
            enemy = array_concat(enemy, ["oMentalNode,50,150,20,150", "oEmitter,3,250,700,800", "oEmitterManager,1,0,0,0"]);
            var reduce = [];
            
            if (zis(32))
                reduce = ["oMutateZ3B,20,300,300,450", "oMutateZ3A,9,400,350,550"];
            
            if (zis(33))
                reduce = ["oMutateZ3B,15,300,350,450", "oMutateZ3A,6,400,450,550", "oSpotfish,8,700,350,450"];
            
            if (array_length(reduce) > 0)
            {
                for (var i = 0; i < array_length(reduce); i++)
                {
                    var keyword = array_get(split_string(reduce[i], ","), 0);
                    
                    for (var j = 0; j < array_length(enemy); j++)
                    {
                        var search = enemy[j];
                        
                        if (string_pos(keyword, search) != 0)
                            enemy[j] = reduce[i];
                    }
                }
            }
        }
    }
    
    if (zis(41))
    {
        if (global.zone4ALT)
            enemy = ["oCrystaling,15,400,300,400", "oCrystalMine,15,400,150,250", "oBoltlet,40,150,50,200", "oBoltfish,25,150,150,350", "oCrystalAttach,15,400,300,500", "oCrystalAmbient,40,400,50,300"];
        else
            enemy = ["oMarrowManager,1,0,0,0", "oCoilframe,6,400,400,600", "oKitelet,100,200,10,130", "oKitefish,25,300,150,250", "oBlazelet,15,100,150,350", "oMarrowBlob,5,400,400,700"];
    }
    else if (zis(42))
    {
        if (global.zone4ALT)
            enemy = ["oCrystaling,15,400,300,450", "oCrystalMine,25,300,250,350", "oBoltlet,40,150,100,150", "oBoltfish,25,150,150,350", "oMutateZ4B,6,300,600,1000", "oCrystalAttach,20,400,300,500", "oCrystalAmbient,50,400,50,300"];
        else
            enemy = ["oMarrowManager,1,0,0,0", "oCoilframe,6,400,400,600", "oKitelet,100,200,10,130", "oKitefish,25,100,150,300", "oBlazelet,15,100,150,450", "oMutateZ4,8,300,400,700", "oMarrowBlob,7,400,400,700"];
    }
    else if (zis(43))
    {
        if (global.zone4ALT)
            enemy = ["oCrystaling,8,400,300,500", "oCrystalMine,25,300,250,350", "oBoltlet,30,150,140,170", "oBoltfish,20,150,150,350", "oMutateZ4B,6,300,600,1000", "oCrystalfish,6,500,780,820", "oCache,1,1500,200,900", "oCrystalAttach,25,400,300,500", "oCrystalAmbient,60,400,50,300"];
        else
            enemy = ["oMarrowManager,1,0,0,0", "oCoilframe,6,400,400,600", "oKitelet,80,200,20,130", "oKitefish,13,100,150,450", "oBlazelet,6,100,300,500", "oMutateZ4,6,300,400,600", "oBlazer,8,200,400,700", "oCache,1,1500,200,900", "oMarrowBlob,7,400,400,700"];
    }
    else if (zis(44))
    {
        if (global.zone4ALT)
        {
            if (exist(oStargazerCutscene))
            {
                SaveSet("QUEST", "STARGAZERFIGHT", -1);
                enemy = ["oBossStargazer,1,150,0,0"];
            }
            else if (SaveGet("ENEMY", "BOSSSTARGAZER") == 1)
            {
                if (RND_step() > 0.5)
                    enemy = ["oBossStargazer,1,150,0,0"];
                else
                    enemy = ["oBossSiphore,1,150,0,0"];
            }
            else
            {
                enemy = ["oBossSiphore,1,150,0,0"];
            }
        }
        else if (exist(oPlayer) && oPlayer.upgrades[UnknownEnum.Value_21] == 1)
        {
            enemy = ["oBossChimera,1,270,0,0"];
        }
        else if (SaveGet("QUEST", "OARFISH") == 1)
        {
            enemy = ["oDrillCrumple,1,270,0,0"];
        }
        else if (RND_step() > 0.5 && SaveGet("ENEMY", "BOSSCHIMERA") == 1)
        {
            enemy = ["oBossChimera,1,270,0,0"];
        }
        else
        {
            enemy = ["oBossDriller,1,270,0,0"];
        }
    }
    
    if (zisc(41, 43) && global.zone4ALT && exist(oPlayer) && oPlayer.upgrades[UnknownEnum.Value_21] == 1 && SaveGet("QUEST", "SATELLITE ENABLED") != 1)
    {
        enemy = array_concat(enemy, ["oMentalNode,50,150,20,150"]);
        
        if (SaveGet("QUEST", "CALLSIGNS") != 99)
            enemy = array_concat(enemy, ["oEmitterStargazer,3,250,700,800"]);
        
        enemy = array_subtract(enemy, ["oMutateZ4B,6,300,600,1000"]);
    }
    
    if (zisc(41, 43) && !global.zone4ALT && exist(oPlayer) && SaveGet("QUEST", "SNIFFER") == 4)
    {
        var reduce = [];
        
        if (zis(42))
            reduce = ["oMutateZ4,8,300,600,900", "oMarrowBlob,7,400,500,900"];
        
        if (zis(43))
            reduce = ["oMutateZ4,6,300,600,900", "oMarrowBlob,7,400,500,900", "oBlazer,8,200,500,900"];
        
        if (array_length(reduce) > 0)
        {
            for (var i = 0; i < array_length(reduce); i++)
            {
                var keyword = array_get(split_string(reduce[i], ","), 0);
                
                for (var j = 0; j < array_length(enemy); j++)
                {
                    var search = enemy[j];
                    
                    if (string_pos(keyword, search) != 0)
                        enemy[j] = reduce[i];
                }
            }
        }
    }
    else if (zis(51))
    {
        enemy = ["oFireField,1,100,0,0", "oChassisGlobal,1,100,0,0", "oLeechling,45,100,80,125", "oLeechfish,15,200,150,200", "oGulletling,6,700,500,700", "oChassis,8,0,600,900", "oDroneMiniSpawn,30,800,230,400"];
    }
    else if (zis(52))
    {
        enemy = ["oFireField,1,100,0,0", "oChassisGlobal,1,100,0,0", "oLeechling,45,100,100,150", "oLeechfish,15,200,150,200", "oGulletling,6,700,500,700", "oChassis,10,100,600,900", "oDroneMiniSpawn,30,50,400,600", "oDroneMaxSpawn,15,200,500,800", "oBossFinal1Fake,1,0,0,0"];
    }
    else if (zis(53))
    {
        enemy = ["oFireField,1,100,0,0", "oChassisGlobal,1,100,0,0", "oLeechling,20,100,200,400", "oLeechfish,20,300,200,400", "oGulletling,6,400,500,800", "oGulletfish,6,700,600,900", "oChassis,10,100,600,900", "oDroneMiniSpawn,30,0,400,800", "oDroneMaxSpawn,15,200,500,800"];
    }
    else if (zis(54))
    {
        enemy = ["oBossFinal1,1,270,0,0"];
    }
    else if (zis(61))
    {
        enemy = ["oRustling,60,200,20,75", "oMutateZ1Fodder2,18,400,100,200", "oMutateZ1C,7,300,300,400", "oMutateZ1D,7,500,300,400", "oMutateZ1A,10,500,300,400", "oMutateZ1B,12,500,400,600", "oCache,1,1000,200,900", "oShootBot,20,0,200,250"];
    }
    else if (zis(62))
    {
        enemy = ["oMutateZ2Fodder1,45,100,120,240", "oMutateZ2Fodder2,15,600,120,250", "oMutateZ2Primary,4,200,600,700", "oMutateZ2Secondary,8,500,400,600", "oMutateZ2Shooter1,12,0,200,400", "oMutateZ2Shooter2,8,400,400,600", "oCache,1,1500,200,900", "oShootBot,20,0,300,400", "oBombBot,20,200,400,500"];
    }
    else if (zis(63))
    {
        enemy = ["oNode,150,150,20,150", "oSpotlet,15,50,300,400", "oMutateZ3B,15,300,250,350", "oMutateZ3A,6,400,350,450", "oMutateZ3N4,4,700,300,400", "oMutateZ3N4,3,2600,250,400", "oSpotfish,8,700,250,350", "oCache,1,1400,200,600", "oBombBot,20,0,300,400", "oLaserBot,20,200,350,450"];
    }
    
    if (zisc(21, 23) && !global.zone2ALT && (zis() % 10) == ((global.seed % 3) + 1))
        array_push(enemy, "oArraysJunk,1,0,0,300");
    
    if (zisc(21, 23) && global.zone2ALT && (zis() % 10) == ((global.seed % 3) + 1))
        array_push(enemy, "oSepticJunk,1,0,0,300");
    
    if (zisc(21, 23) && !global.zone2ALT && SaveGet("QUEST", "SNIFFER") == 1)
        array_push(enemy, "oSnifferIllusionManager,1,0,0,0");
    
    if (zisc(21, 23) && global.zone2ALT && SaveGet("QUEST", "KITBASH") == 1)
    {
        if (zis(21))
            array_push(enemy, "oKitbashJunk,2,1000,400,600");
        
        if (zis(22))
            array_push(enemy, "oKitbashJunk,2,800,400,600");
        
        if (zis(23))
            array_push(enemy, "oKitbashJunk,1,800,400,600");
    }
    
    if (zis(UnknownEnum.Value_45))
    {
        var deep = SaveGet("QUEST", "DEEP LATTICE");
        
        if (deep <= 0)
            enemy = ["oCrystaling,15,400,300,400", "oCrystalMine,15,400,150,250", "oBoltlet,40,150,50,200", "oBoltfish,25,150,150,350", "oCrystalAttach,15,400,300,500", "oCrystalAmbient,40,400,50,300", "oGlitchWave,1,1000,0,0"];
        else if (deep == 1)
            enemy = ["oCrystaling,15,400,300,450", "oCrystalMine,25,300,250,350", "oBoltlet,40,150,100,150", "oBoltfish,25,150,150,350", "oCrystalAttach,20,400,300,500", "oCrystalAmbient,50,400,50,300", "oGlitchWave,2,500,700,700"];
        else if (deep == 2)
            enemy = ["oDroneMaxQ,8,400,400,700", "oCrystalMine,25,300,250,350", "oBoltlet,30,150,140,170", "oBoltfish,20,150,150,350", "oCrystalfish,6,500,780,820", "oCrystalAttach,25,400,300,500", "oCrystalAmbient,60,400,50,300", "oGlitchWave,2,500,800,1000"];
        else if (deep == 3)
            enemy = ["oDroneMaxQ,8,400,400,700", "oCrystalMine,25,300,250,350", "oBoltlet,30,150,140,170", "oBoltfish,20,150,150,350", "oCrystalfish,6,500,780,820", "oCrystalAttach,25,400,300,500", "oCrystalAmbient,60,400,50,300", "oGlitchWave,2,500,800,1000"];
    }
    
    if (zis(UnknownEnum.Value_m108))
        enemy[0] = "oTutorialFish,20,200,20,65";
    
    return enemy;
}

enum UnknownEnum
{
    Value_m108 = -108,
    Value_21 = 21,
    Value_45 = 45
}

"""

enemy_list = []
data = data.splitlines("\n")

for line in data:
    if '"o' in line:
        for text in line.strip().split('"'):
            if "o" in text and "Boss" in text and "oCache" not in text and "=" not in text:
                enemy_list.append(text)

print(str(enemy_list).replace("'", '"'))
print(len(enemy_list))