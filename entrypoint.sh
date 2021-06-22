
# 日志需要先创建 logs 文件夹
mkdir -p logs

# 是否需要执行数据库变更
if [ "$ENABLE_MIGRATE" == "true" ];then
  python3 manage.py migrate
fi


echo "start demo web service"

# 根据配置环境指定运行方式
if [ "$ENV" == "local" ];then
  exec python3 manage.py runserver 0.0.0.0:8080
else
  # 生产环境容器每次都是重新构建
  python3 manage.py collectstatic
  exec gunicorn demo.wsgi:application \
    --name main_django \
    --max-requests 2000 \
    --max-requests-jitter 500 \
    --bind 0.0.0.0:8080 \
    --workers 4 \
    --threads 4 \
    "$@"
fi

