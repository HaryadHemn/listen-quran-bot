from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("OTU5Nzg0MjA3OTE0MjQ2MTU0.GuXWsm.LiOmGg2WP_N3ubPqYAWdRqQXceYt2L5HMOEGhc")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
