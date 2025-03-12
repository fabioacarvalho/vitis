Using Redis:

Para utilizar o cache o Django disponibiliza um decorator @chace_page() ele precisa ser importado de from dango.views.decorators.cache import cache_page e para definir o tempo de cache, passamos dentro do page o tempo em segundos @chace_page(60) neste caso será cacheado por 60 segundos.