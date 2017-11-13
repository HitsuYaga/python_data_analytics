$(document).ready(function ($) {
  if ($("#notfound").length) {
    alert("Login fail. Please check your info and try again.")
    window.location.assign('/')
  }

  // Toogle form /////////////////////////////////////////////////
  $('.form-query').hide();
  $('.get-config').on('click', function () {
    $('.form-query').toggle('slow');
    $('.form-create').hide();
    $('.form-delete').hide();
    $('.form-test').hide();
    $('.form-elasticsearch').hide();
  })

  $('.form-create').hide();
  $('.post-config').on('click', function () {
    $('.form-create').toggle('slow');
    $('.form-query').hide();
    $('.form-delete').hide();
    $('.form-test').hide();
    $('.form-elasticsearch').hide();
  })

  $('.form-delete').hide();
  $('.delete-config').on('click', function () {
    $('.form-delete').toggle('slow');
    $('.form-query').hide();
    $('.form-create').hide();
    $('.form-test').hide();
    $('.form-elasticsearch').hide();
  })

  $('.form-test').hide();
  $('.test-config').on('click', function () {
    $('.form-test').toggle('slow');
    $('.form-query').hide();
    $('.form-create').hide();
    $('.form-delete').hide();
    $('.form-elasticsearch').hide();
  })

  $('.form-elasticsearch').hide();
  $('.elasticsearch-config').on('click', function () {
    $('.form-elasticsearch').toggle('slow');
    $('.form-query').hide();
    $('.form-create').hide();
    $('.form-delete').hide();
    $('.form-test').hide();
  })

  // Affect when option selected /////////////////////////////////
  $('.query-type').change(function () {
    $('.query-name').show();
    var option = $('.query-type option:selected').text()
    if (option == "Global") {
      $('.query-name').hide();
      $('.query-name input').removeAttr('required');
    }
  })

  //////////////////////////////////////////////////////////////////
  var parser_schema_ex = {
    "parserClassName": "org.apache.metron.parsers.GrokParser",
    "sensorTopic": "testing",
    "parserConfig": {
      "grokPath": "/apps/metron/patterns/testing",
      "patternLabel": "TESTING_DELIMITED",
      "timestampField": "timestamp"
    }
  }

  var enrichment_schema_ex = {
    "enrichment": {
      "fieldMap": {
        "stellar": {
          "config": {}
        }
      },
      "fieldToTypeMap": {},
      "config": {}
    },
    "configuration": {}
  }

  var indexing_schema_ex = {
    "hdfs": {
      "index": "testing",
      "batchSize": 5,
      "enabled": false
    },
    "elasticsearch": {
      "index": "testing",
      "batchSize": 1,
      "enabled": true
    },
    "solr": {
      "index": "testing",
      "batchSize": 5,
      "enabled": false
    }
  }

  var grok_pattern_ex = "TESTING_DELIMITED %{NOTSPACE:timestamp} %{IP:client} %{WORD:method} \
%{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}"

  var kafka_topic_ex = {
    "name": "testing",
    "numPartitions": 1,
    "replicationFactor": 1,
    "properties": {}
  }

  var sample_data_test = "1467011176 55.3.244.1 GET /index.html 15824 0.043"

  $("textarea#exampleFormControlTextarea1").val(JSON.stringify(parser_schema_ex, undefined, 4));

  $('.create-type').change(function () {
    $('.create-name').show();
    $('.config-data').show();
    var option = $('.create-type option:selected').text()
    if (option == "Enrichment") {
      $("textarea#exampleFormControlTextarea1").val(JSON.stringify(enrichment_schema_ex, undefined, 4));
    } else if (option == "Indexing") {
      $("textarea#exampleFormControlTextarea1").val(JSON.stringify(indexing_schema_ex, undefined, 4));
    } else if (option == "Grok Pattern") {
      $("textarea#exampleFormControlTextarea1").val(grok_pattern_ex);
    } else if (option == "Kafka Topic") {
      $('.create-name').hide();
      $('.create-name input').removeAttr('required');
      $("textarea#exampleFormControlTextarea1").val(JSON.stringify(kafka_topic_ex, undefined, 4));
    } else if (option == "Topology") {
      $('.config-data').hide();
    }
  })

  $("textarea.data-sample").val(sample_data_test);
})