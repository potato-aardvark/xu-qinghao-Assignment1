import random

class Ship:
    def __init__(self, name):
        """Create new ship, with name name."""
        self.name = name
        self._hullstrength = 2.
        self._shieldstrength = 1.
        self._laser_power = 1.
        self._isdead = False
    
    def __repr__(self):
        return str(self._isdead)
    
    def get_name(self):
        """get name"""
        return self.name
    
    def get_laser_power(self):
        """get laser power"""
        return self._laser_power
    
    def fire_at(self, target):
        """Fire laser at target, and print message."""
        print('{me} fires a laser at {them}!'.format(me=self.name, them=target.name))
        target.is_fired_at_by(self, 'laser', self.get_laser_power())
    
    def is_dead(self):
        """get whether self is dead"""
        return self._isdead
    
    def is_fired_at_by(self, origin, attack_type, power):
        """Handle being targeted by an attack described by str attack_type 
        (e.g., 'laser', 'missile'), dealing power damage."""
        msg_hull_hit = False
        msg_hull_destroyed = False
        msg_shield_destroyed = False
        msg_shield_hit = False
        
        damage_dealt = -1
        
        if self._shieldstrength > power:
            msg_shield_hit = True
            self._shieldstrength -= power
            damage_dealt = power
        elif self._shieldstrength > 0.:
            msg_shield_destroyed = True
            self._shieldstrength = 0.
        elif self._hullstrength > power / 2:
            msg_hull_hit = True
            self._hullstrength -= power / 2
            damage_dealt = power / 2
        elif self._hullstrength > 0.:
            msg_hull_destroyed = True
            self._hullstrength = 0.
            self.isdead = True
             
        print('The {atk} from {them} strikes {me},'.format(
            me=self.name, them=origin.name, atk=attack_type
            ), 
            end=' '
        )
        if msg_shield_hit:
            print('striking the shield and dealing {dmg} damage!'.format(dmg=damage_dealt))
        elif msg_shield_destroyed:
            print('destroying the shields and exposing the hull!')
        elif msg_hull_hit:
            print('striking the hull and dealing {dmg} damage!'.format(dmg=damage_dealt))
        elif msg_hull_destroyed:
            print('destroying the hull! {me} has been shot down.'.format(me=self.name))

class Warship(Ship):
    def __init__(self, name):
        super(Warship, self).__init__(name)
        self._missile_strength = 2.
    
    def get_missile_power(self):
        return 2. 
    
    def fire_at(self, target):
        if random.random() < 0.3:
            print('{me} fires a missile at {them}!'.format(me=self.name, them=target.name))
            target.is_fired_at_by(self, 'missile', self.get_missile_power())
        else:
            super(Warship, self).fire_at(target)

class Speeder(Ship):
    def is_fired_at_by(self, origin, attack_type, power):
        if random.random() < 0.5:
            print('{me} evades the attack!'.format(me=self.name))
        else:
            super(Speeder, self).is_fired_at_by(origin, attack_type, power)

ships = [Ship("Alpha 1"), Ship("Beta 2"), Ship("Gamma 9"), Warship("Omega 10"), Speeder("Sigma 7")]
while len(ships) > 1:
    involveds = random.sample(ships, 2)
    print(ships)
    involveds[0].fire_at(involveds[1])
    ships = [ship for ship in ships if not ship.is_dead()]

print('{} wins!'.format(ships[0]))