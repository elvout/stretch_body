import unittest
import stretch_body.trajectories


class TestTrajectories(unittest.TestCase):

    def test_waypoint(self):
        print('equal')
        w1 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0); print('w1: {0}'.format(w1))
        w2 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0); print('w2: {0}'.format(w2))
        self.assertEqual(w1, w2)

        print('not equal')
        w1 = stretch_body.trajectories.Waypoint(time=1.0, position=0.0); print('w1: {0}'.format(w1))
        w2 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0); print('w2: {0}'.format(w2))
        self.assertNotEqual(w1, w2)

        print('equal')
        w1 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0, velocity=0.0); print('w1: {0}'.format(w1))
        w2 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0); print('w2: {0}'.format(w2))
        self.assertEqual(w1, w2)

        print('equal')
        w1 = stretch_body.trajectories.Waypoint(time=1.0, position=0.0, velocity=1000, acceleration=43, contact_threshold=10); print('w1: {0}'.format(w1))
        w2 = stretch_body.trajectories.Waypoint(time=1.0, position=0.0, velocity=1000, acceleration=43, contact_threshold=10); print('w2: {0}'.format(w2))
        self.assertEqual(w1, w2)

        print('not equal')
        w1 = stretch_body.trajectories.Waypoint(time=1.0, position=0.0, velocity=3249, acceleration=43, contact_threshold=10); print('w1: {0}'.format(w1))
        w2 = stretch_body.trajectories.Waypoint(time=1.1, position=0.0, velocity=1000, acceleration=43); print('w2: {0}'.format(w2))
        self.assertNotEqual(w1, w2)

    def test_invalid_waypoints(self):
        with self.assertRaises(ValueError):
            stretch_body.trajectories.Waypoint(time=None, position=None)

        with self.assertRaises(ValueError):
            stretch_body.trajectories.Waypoint(time=0.0, position=None)

        with self.assertRaises(ValueError):
            stretch_body.trajectories.Waypoint(time=1.0, position=0.0, acceleration=43)

    def test_waypoint_operations(self):
        w1 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0)
        w2 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0)
        self.assertTrue(w1 == w2)
        self.assertFalse(w1 != w2)
        self.assertFalse(w1 < w2)
        self.assertFalse(w1 > w2)
        self.assertTrue(w1 <= w2)
        self.assertTrue(w1 >= w2)

        w1 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0)
        w2 = stretch_body.trajectories.Waypoint(time=0.001, position=0.0)
        self.assertTrue(w1 == w2)
        self.assertFalse(w1 != w2)
        self.assertTrue(w1 < w2)
        self.assertFalse(w1 > w2)
        self.assertTrue(w1 <= w2)
        self.assertFalse(w1 >= w2)

        w1 = stretch_body.trajectories.Waypoint(time=0.0, position=0.0)
        w2 = stretch_body.trajectories.Waypoint(time=0.1, position=0.0)
        self.assertFalse(w1 == w2)
        self.assertTrue(w1 != w2)
        self.assertTrue(w1 < w2)
        self.assertFalse(w1 > w2)
        self.assertTrue(w1 <= w2)
        self.assertFalse(w1 >= w2)

    def test_segment(self):
        print('equal')
        s1 = stretch_body.trajectories.Segment(segment_id=0, duration=0.0, a0=0.0, a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0); print('s1: {0}'.format(s1))
        s2 = stretch_body.trajectories.Segment(segment_id=1, duration=0.0, a0=0.0, a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0); print('s2: {0}'.format(s2))
        self.assertEqual(s1, s2)

        print('not equal')
        s1 = stretch_body.trajectories.Segment(segment_id=0, duration=0.0, a0=0.0, a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0); print('s1: {0}'.format(s1))
        s2 = stretch_body.trajectories.Segment(segment_id=1, duration=0.0, a0=0.0, a1=100.0, a2=-34.0, a3=0.0, a4=0.0, a5=0.0); print('s2: {0}'.format(s2))
        self.assertNotEqual(s1, s2)

        print('not equal')
        segment_arr = [3.0, 62.425, 0, 0, -3.731, 1.866, -0.249]
        s1 = stretch_body.trajectories.Segment.from_array(segment_arr, segment_id=0); print('s1: {0}'.format(s1))
        s2 = stretch_body.trajectories.Segment(segment_id=1, duration=0.0, a0=0.0, a1=100.0, a2=-34.0, a3=0.0, a4=0.0, a5=0.0); print('s2: {0}'.format(s2))
        self.assertNotEqual(s1, s2)

        print('equal')
        segment_arr = [3.0, 62.425, 0, 0, -3.731, 1.866, -0.249]
        s1 = stretch_body.trajectories.Segment.from_array(segment_arr, segment_id=0); print('s1: {0}'.format(s1))
        s2 = stretch_body.trajectories.Segment(segment_id=1, duration=3.0, a0=62.425, a1=0.0, a2=0.0, a3=-3.731, a4=1.866, a5=-0.249); print('s2: {0}'.format(s2))
        self.assertEqual(s1, s2)

        print('equal')
        s1_arr = [3.0, 62.425, 0, 0, -3.731, 1.866, -0.249, 0]; print('s1: {0}'.format(s1_arr))
        s2_arr = stretch_body.trajectories.Segment(segment_id=0, duration=3.0, a0=62.425, a1=0.0, a2=0.0, a3=-3.731, a4=1.866, a5=-0.249).to_array(); print('s2: {0}'.format(s2_arr))
        self.assertEqual(s1_arr, s2_arr)

        print('equal')
        s1_arr = [62.425, 0, 0, -3.731, 1.866, -0.249]; print('s1: {0}'.format(s1_arr))
        s2_arr = stretch_body.trajectories.Segment(segment_id=1, duration=3.0, a0=62.425, a1=0.0, a2=0.0, a3=-3.731, a4=1.866, a5=-0.249).to_array(only_coeffs=True); print('s2: {0}'.format(s2_arr))
        self.assertEqual(s1_arr, s2_arr)

        print('equal')
        s1 = stretch_body.trajectories.Segment.zeros(); print('s1: {0}'.format(s1))
        s2 = stretch_body.trajectories.Segment(segment_id=1, duration=0.0, a0=0.0, a1=0.0, a2=0.0, a3=0.0, a4=0.0, a5=0.0); print('s2: {0}'.format(s2))
        self.assertEqual(s1, s2)

    def test_from_invalid_segment_arr(self):
        segment_arr = [4, 65]
        with self.assertRaises(ValueError):
            stretch_body.trajectories.Segment.from_array(segment_arr)

        segment_arr = [4, 65, 4, 56, 36, 346, 345, 345, 346, 346, 234, 23]
        with self.assertRaises(ValueError):
            stretch_body.trajectories.Segment.from_array(segment_arr)

    def test_segment_evaluate_at(self):
        """Verify correctness of the Segment.evaluate_at method

        Spline coefficients calculated in Desmos at:
        https://www.desmos.com/calculator/atv5ilhodq
        """
        # Segment b
        b1 = stretch_body.trajectories.Waypoint(time=0.0, position=62.425, velocity=0.0, acceleration=0.0)
        b2 = stretch_body.trajectories.Waypoint(time=3.0, position=52.350, velocity=0.0, acceleration=0.0)
        b  = stretch_body.trajectories.Segment(segment_id=2, duration=3.0, a0=62.425, a1=0, a2=0, a3=-3.7314815, a4=1.8657407, a5=-0.2487654)

        pos, vel, accel = b.evaluate_at(b1.time - b1.time)
        self.assertAlmostEqual(pos, b1.position, places=4)
        self.assertAlmostEqual(vel, b1.velocity, places=4)
        self.assertAlmostEqual(accel, b1.acceleration, places=4)

        pos, vel, accel = b.evaluate_at(b2.time - b1.time)
        self.assertAlmostEqual(pos, b2.position, places=4)
        self.assertAlmostEqual(vel, b2.velocity, places=4)
        self.assertAlmostEqual(accel, b2.acceleration, places=4)

        pos, vel, accel = b.evaluate_at(1.3 - b1.time)
        self.assertAlmostEqual(pos, 58.632, places=3)
        self.assertNotAlmostEqual(vel, 0.0, places=4)
        self.assertNotAlmostEqual(accel, 0, places=4)

        # Segment c
        c1 = stretch_body.trajectories.Waypoint(time=3.0, position=52.350, velocity=0.0, acceleration=0.0)
        c2 = stretch_body.trajectories.Waypoint(time=6.0, position=62.425, velocity=0.0, acceleration=0.0)
        c  = stretch_body.trajectories.Segment(segment_id=3, duration=3.0, a0=52.350, a1=0, a2=0, a3=3.7314815, a4=-1.8657407, a5=0.2487654)
        pos, vel, accel = c.evaluate_at(c1.time - c1.time)
        self.assertAlmostEqual(pos, c1.position, places=4)
        self.assertAlmostEqual(vel, c1.velocity, places=4)
        self.assertAlmostEqual(accel, c1.acceleration, places=4)

        pos, vel, accel = c.evaluate_at(c2.time - c1.time)
        self.assertAlmostEqual(pos, c2.position, places=4)
        self.assertAlmostEqual(vel, c2.velocity, places=4)
        self.assertAlmostEqual(accel, c2.acceleration, places=4)

        pos, vel, accel = c.evaluate_at(4.584 - c1.time)
        self.assertAlmostEqual(pos, 57.915, places=3)
        self.assertNotAlmostEqual(vel, 0.0, places=4)
        self.assertNotAlmostEqual(accel, 0, places=4)
